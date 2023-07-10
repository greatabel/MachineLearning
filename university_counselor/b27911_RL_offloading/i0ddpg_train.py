import tensorflow.keras.optimizers as optimizers
from i2common import *


def train_model(
    env,
    actor_model,
    critic_model,
    target_actor_model,
    target_critic_model,
    actor_optimizer,
    critic_optimizer,
    num_episodes=300,
    batch_size=64,
    gamma=0.99,
    tau=0.001,
):

    print("开始训练模型")
    buffer = ReplayBuffer()

    for i in range(num_episodes):
        state = env.reset()
        done = False
        print(i)
        while not done:
            # 由演员模型选择一个动作
            action = actor_model.predict(np.array([state]))[0]

            # 执行动作并获取 next_state, reward 和 done
            next_state, reward, done, _ = env.step(action)

            # 将经验存入缓存
            buffer.record((state, action, reward, next_state, done))

            # 如果缓冲区足够大，开始训练
            if len(buffer.buffer) > batch_size:
                experiences = buffer.sample(batch_size)
                states, actions, rewards, next_states, dones = zip(*experiences)

                states = np.array(states)
                actions = np.array(actions)
                rewards = np.array(rewards)
                next_states = np.array(next_states)
                dones = np.array(dones)

                # 更新评论者模型
                target_q_values = critic_model.predict(
                    [next_states, actor_model.predict(next_states)]
                )
                q_values = rewards + gamma * target_q_values * (1 - dones)

                critic_loss = critic_model.train_on_batch([states, actions], q_values)

                # 更新演员模型
                with tf.GradientTape() as tape:
                    actions = actor_model(states)
                    critic_value = critic_model([states, actions])

                    # 使用 `-value` 是因为我们想最大化评论者模型为我们的动作给出的价值
                    actor_loss = -tf.math.reduce_mean(critic_value)

                actor_grad = tape.gradient(actor_loss, actor_model.trainable_variables)
                actor_optimizer.apply_gradients(
                    zip(actor_grad, actor_model.trainable_variables)
                )

                # 更新冻结目标模型
                for (model_weights, target_weights) in zip(
                    actor_model.get_weights(), target_actor_model.get_weights()
                ):
                    target_weights = tau * model_weights + (1 - tau) * target_weights

                for (model_weights, target_weights) in zip(
                    critic_model.get_weights(), target_critic_model.get_weights()
                ):
                    target_weights = tau * model_weights + (1 - tau) * target_weights

        # 跑一段时间，打印一些信息
        if i % 100 == 0:
            print(f"已完成 {i} 回合")

    actor_model.save_weights("actor_model_weights.h5")
    critic_model.save_weights("critic_model_weights.h5")


def main():
    env = EdgeComputingEnv()

    actor_model = create_actor_model(env.state_dim, env.action_dim)
    critic_model = create_critic_model(env.state_dim, env.action_dim)
    target_actor_model = create_actor_model(env.state_dim, env.action_dim)
    target_critic_model = create_critic_model(env.state_dim, env.action_dim)

    actor_optimizer = tf.keras.optimizers.Adam()
    critic_optimizer = tf.keras.optimizers.Adam()

    critic_model.compile(loss="mse", optimizer=critic_optimizer)

    train_model(
        env,
        actor_model,
        critic_model,
        target_actor_model,
        target_critic_model,
        actor_optimizer,
        critic_optimizer,
    )


if __name__ == "__main__":
    main()
