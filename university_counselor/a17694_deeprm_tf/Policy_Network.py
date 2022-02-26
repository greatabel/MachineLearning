import numpy as np
import tensorflow as tf

np.random.seed(1)
tf.set_random_seed(1)

from functools import reduce
from operator import mul


class PolicyGradient:
    def __init__(
        self,
        n_actions,
        n_features,
        learning_rate=0.01,
        output_graph=False,
    ):
        self.n_actions = n_actions
        self.n_features = n_features
        self.lr = learning_rate
        self.gamma = 0.96

        self.ep_obs, self.ep_as, self.ep_rs = [], [], []

        self._build_net()

        self.sess = tf.Session()
        self.saver = tf.train.Saver()

        if output_graph:

            tf.summary.FileWriter("logs/", self.sess.graph)

        self.sess.run(tf.global_variables_initializer())

    def _build_net(self):
        with tf.name_scope("inputs"):
            self.tf_obs = tf.placeholder(
                tf.float32, [None, self.n_features], name="observations"
            )
            self.tf_acts = tf.placeholder(
                tf.int32,
                [
                    None,
                ],
                name="actions_num",
            )
            self.tf_vt = tf.placeholder(
                tf.float32,
                [
                    None,
                ],
                name="actions_value",
            )
        # 构建传入数据第1层
        layer = tf.layers.dense(
            inputs=self.tf_obs,
            units=10,
            activation=tf.nn.tanh,  # tanh activation
            kernel_initializer=tf.random_normal_initializer(mean=0, stddev=0.3),
            bias_initializer=tf.constant_initializer(0.1),
        )
        # 构建传入数据第2层
        all_act = tf.layers.dense(
            inputs=layer,
            units=self.n_actions,
            activation=None,
            kernel_initializer=tf.random_normal_initializer(mean=0, stddev=0.3),
            bias_initializer=tf.constant_initializer(0.1),
        )
        # 使用softmax转换为概率
        self.all_act_prob = tf.nn.softmax(all_act, name="act_prob")

        with tf.name_scope("loss"):
            # 最大化总奖励（log_p * R）是最小化-（log_p * R），并且tf只有minimize（loss）
            neg_log_prob = tf.nn.sparse_softmax_cross_entropy_with_logits(
                logits=all_act, labels=self.tf_acts
            )

            self.loss = tf.reduce_mean(neg_log_prob * self.tf_vt)  # reward guided loss

        with tf.name_scope("train"):
            self.train_op = tf.train.AdamOptimizer(self.lr).minimize(self.loss)

    def choose_action(self, observation):
        prob_weights = self.sess.run(
            self.all_act_prob, feed_dict={self.tf_obs: observation}
        )
        # 选择动作 w.r.t 动作概率
        action = np.random.choice(range(prob_weights.shape[1]), p=prob_weights.ravel())
        return action

    def store_ob(self, s):
        self.ep_obs.append(s)

    def store_action(self, a):
        self.ep_as.append(a)

    def store_adv(self, r):
        self.ep_rs.append(r)

    def learn(self, all_ob, all_action, all_adv):

        _, loss = self.sess.run(
            [self.train_op, self.loss],
            feed_dict={
                self.tf_obs: np.array(all_ob),  # shape=[None, n_obs]
                self.tf_acts: np.array(all_action),  # shape=[None, ]
                self.tf_vt: np.array(all_adv),  # shape=[None, ]
            },
        )

        self.ep_obs, self.ep_as, self.ep_rs = [], [], []  # empty episode data
        return loss

    def _discount_and_norm_rewards(self):

        discounted_ep_rs = np.fabs(np.array(self.ep_rs))

        return discounted_ep_rs

    def save_data(self, pg_resume):
        self.saver.save(self.sess, pg_resume + ".ckpt")

    def load_data(self, pg_resume):
        self.saver.restore(self.sess, pg_resume)

    def get_num_params(self):
        num_params = 0
        for variable in tf.trainable_variables():
            shape = variable.get_shape()
            num_params += reduce(mul, [dim.value for dim in shape], 1)
        return num_params
