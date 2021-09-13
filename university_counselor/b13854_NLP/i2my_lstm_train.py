import os
import json
import gc
import pickle

import numpy as np
import pandas as pd
from tqdm import tqdm_notebook as tqdm
from tensorflow.keras.models import Model
from tensorflow.keras.layers import (
    Input,
    Dense,
    Embedding,
    SpatialDropout1D,
    concatenate,
    Masking,
)
from tensorflow.keras.layers import LSTM, Bidirectional, GlobalMaxPooling1D, Dropout
from tensorflow.keras.preprocessing import text, sequence
from tqdm import tqdm_notebook as tqdm
import fasttext
import gensim

"""
主要思路是把维基百科文章（去掉标签后）当作文档，
将每个文档分解为与每个候选长答案相对应的部分。
然后，如果它是真正的长答案，我将每个长答案标记为 
1，否则标记为 0。对于每一行，我还包括问题和 example_id。
然后，我训练一个 LSTM 来利用历史来预测未来该标签的位置

然后调用整个model对数据集训练，训练结束后在test集做测试

根据标记器的索引生成快速文本嵌入（ FAIR  Python API）。
构建两个2层双向LSTM；一层读问题，另一个读维基百科正文。
使用 Sigmoid 激活预测二进制输出。
使用2元交叉熵损失进行优化。
为了运行速度，保存model
我们首先删除所有置信度太低部分，
然后对于每个 example_id，我们只保留置信度最高的行作为输出。
"""


def my_build_train(train_path, n_rows=200000, sampling_rate=15):
    with open(train_path) as f:
        processed_rows = []

        for i in tqdm(range(n_rows)):
            line = f.readline()
            if not line:
                break

            line = json.loads(line)

            text = line["document_text"].split(" ")
            question = line["question_text"]
            annotations = line["annotations"][0]

            for i, candidate in enumerate(line["long_answer_candidates"]):
                label = i == annotations["long_answer"]["candidate_index"]

                start = candidate["start_token"]
                end = candidate["end_token"]

                if label or (i % sampling_rate == 0):
                    processed_rows.append(
                        {
                            "text": " ".join(text[start:end]),
                            "is_long_answer": label,
                            "question": question,
                            "annotation_id": annotations["annotation_id"],
                        }
                    )

        train = pd.DataFrame(processed_rows)

        return train


def my_build_test(test_path):
    with open(test_path) as f:
        processed_rows = []

        for line in tqdm(f):
            line = json.loads(line)

            text = line["document_text"].split(" ")
            question = line["question_text"]
            example_id = line["example_id"]

            for candidate in line["long_answer_candidates"]:
                start = candidate["start_token"]
                end = candidate["end_token"]

                processed_rows.append(
                    {
                        "text": " ".join(text[start:end]),
                        "question": question,
                        "example_id": example_id,
                        "sequence": f"{start}:{end}",
                    }
                )

        test = pd.DataFrame(processed_rows)

    return test


def compute_text_and_questions(train, test, tokenizer):
    train_text = tokenizer.texts_to_sequences(train.text.values)
    train_questions = tokenizer.texts_to_sequences(train.question.values)
    test_text = tokenizer.texts_to_sequences(test.text.values)
    test_questions = tokenizer.texts_to_sequences(test.question.values)

    train_text = sequence.pad_sequences(train_text, maxlen=300)
    train_questions = sequence.pad_sequences(train_questions)
    test_text = sequence.pad_sequences(test_text, maxlen=300)
    test_questions = sequence.pad_sequences(test_questions)

    return train_text, train_questions, test_text, test_questions


def build_embedding_matrix(tokenizer, path):
    embedding_matrix = np.zeros((tokenizer.num_words + 1, 300))

    # only this way worked in new version
    ft_model = gensim.models.KeyedVectors.load_word2vec_format(path, binary=False)

    # ft_model = fasttext.load_model(path)

    for word, i in tokenizer.word_index.items():
        if i >= tokenizer.num_words - 1:
            break
        # embedding_matrix[i] = ft_model.get_word_vector(word)
        if word in ft_model:
            r = ft_model[word]
            embedding_matrix[i] = r

    return embedding_matrix


def construct_model(embedding_matrix):
    embedding = Embedding(
        *embedding_matrix.shape,
        weights=[embedding_matrix],
        trainable=False,
        mask_zero=True,
    )

    q_in = Input(shape=(None,))
    q = embedding(q_in)
    q = SpatialDropout1D(0.2)(q)
    q = Bidirectional(LSTM(100, return_sequences=True))(q)
    q = GlobalMaxPooling1D()(q)

    t_in = Input(shape=(None,))
    t = embedding(t_in)
    t = SpatialDropout1D(0.2)(t)
    t = Bidirectional(LSTM(150, return_sequences=True))(t)
    t = GlobalMaxPooling1D()(t)

    hidden = concatenate([q, t])
    hidden = Dense(300, activation="relu")(hidden)
    hidden = Dropout(0.5)(hidden)
    hidden = Dense(300, activation="relu")(hidden)
    hidden = Dropout(0.5)(hidden)

    out1 = Dense(1, activation="sigmoid")(hidden)

    model = Model(inputs=[t_in, q_in], outputs=out1)
    model.compile(loss="binary_crossentropy", optimizer="adam")

    return model


def my_tokenizer():
    """"""


if __name__ == "__main__":
    directory = "data/"
    train_path = directory + "mytrain.jsonl"
    test_path = directory + "mytest.jsonl"

    train = my_build_train(train_path)
    test = my_build_test(test_path)

    print(train.head())
    print(test.head())

    tokenizer = text.Tokenizer(lower=False, num_words=80000)

    for text in tqdm([train.text, test.text, train.question, test.question]):
        tokenizer.fit_on_texts(text.values)
    train_target = train.is_long_answer.astype(int).values

    train_text, train_questions, test_text, test_questions = compute_text_and_questions(
        train, test, tokenizer
    )
    # del train

    path = "wiki-news-300d-1M.vec"
    embedding_matrix = build_embedding_matrix(tokenizer, path)
    model = construct_model(embedding_matrix)
    model.summary()
    train_history = model.fit(
        [train_text, train_questions],
        train_target,
        epochs=2,
        validation_split=0.2,
        batch_size=1024,
    )
    # 2轮的人为分的训练集和测试集交叉验证：
    # Epoch 1/2
    # 4/4 [==============================] - 25s 5s/step - loss: 0.5107 - val_loss: 0.2052
    # Epoch 2/2
    # 4/4 [==============================] - 17s 4s/step - loss: 0.2849 - val_loss: 0.1835

    # 3轮的误差交叉验证：
    # Epoch 1/3
    # 4/4 [==============================] - 25s 5s/step - loss: 0.5254 - val_loss: 0.2169
    # Epoch 2/3
    # 4/4 [==============================] - 16s 4s/step - loss: 0.2729 - val_loss: 0.1836
    # Epoch 3/3
    # 4/4 [==============================] - 16s 4s/step - loss: 0.2748 - val_loss: 0.1662

    # .......
    # .......
    # .......

    # 测试手动过各种轮数, 达到最平衡的在：
    # 最好结果是 4/4 [==============================] - 16s 4s/step - loss: 0.1487 - val_loss: 0.1145
    # Epoch 22/100

    ####################

    with open("tokenizer.pickle", "wb") as handle:
        pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)
    model.save("model.h5")
