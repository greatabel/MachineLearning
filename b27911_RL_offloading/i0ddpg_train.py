import tensorflow.keras.optimizers as optimizers
from abel1 import *


def train_model(env, actor_model, critic_model, target_actor_model, target_critic_model, actor_optimizer, critic_optimizer, num_episodes=300, batch_size=64, gamma=0.99, tau=0.001):
 
    print('train_model')
    buffer = ReplayBuffer()

    for i in range(num_episodes):
        state = env.reset()
        done = False
        print(i)
        while not done:
            # Actor chooses an action
            action = actor_model.predict(np.array([state]))[0]

            # Perform the action and get the next_state, reward and done
            next_state, reward, done, _ = env.step(action)

            # Record the experience into the buffer
            buffer.record((state, action, reward, next_state, done))

            # If buffer is large enough, start training
            if len(buffer.buffer) > batch_size:
                experiences = buffer.sample(batch_size)
                states, actions, rewards, next_states, dones = zip(*experiences)

                states = np.array(states)
                actions = np.array(actions)
                rewards = np.array(rewards)
                next_states = np.array(next_states)
                dones = np.array(dones)

                # Update critic
                target_q_values = critic_model.predict([next_states, actor_model.predict(next_states)])
                q_values = rewards + gamma * target_q_values * (1 - dones)

                critic_loss = critic_model.train_on_batch([states, actions], q_values)

                # Update actor
                with tf.GradientTape() as tape:
                    actions = actor_model(states)
                    critic_value = critic_model([states, actions])
                    # Used `-value` as we want to maximize the value given by the critic for our actions
                    actor_loss = -tf.math.reduce_mean(critic_value)

                actor_grad = tape.gradient(actor_loss, actor_model.trainable_variables)
                actor_optimizer.apply_gradients(zip(actor_grad, actor_model.trainable_variables))

                # Update the Frozen Target Models
               # Update the Frozen Target Models
                for (model_weights, target_weights) in zip(actor_model.get_weights(), target_actor_model.get_weights()):
                    target_weights = tau * model_weights + (1 - tau) * target_weights

                for (model_weights, target_weights) in zip(critic_model.get_weights(), target_critic_model.get_weights()):
                    target_weights = tau * model_weights + (1 - tau) * target_weights
 

        # Print some information
        if i % 100 == 0:
            print(f"Episode {i} finished")

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

    critic_model.compile(loss='mse', optimizer=critic_optimizer)
    
    train_model(env, actor_model, critic_model, target_actor_model, target_critic_model, actor_optimizer, critic_optimizer)

main()