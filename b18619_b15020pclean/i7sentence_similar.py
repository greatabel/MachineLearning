from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
import numpy
from termcolor import colored, cprint


if __name__ == "__main__":

    raw_documents = [
        "Are there any new coronavirus patients in the hospital?",
        "Both COVID-19 and the flu cause respiratory illness, but there are important differences between the two viruses and how they spread",
        "How many hospital beds are there? Are there enough beds for us to get through the pandemic?",
        "The hospital's pharmacy is well-supplied and everything is in order",
        "Emotions of patients with new coronary pneumonia are stable, and everything is in order in the hospital",
        "How can I increase the speed of my internet connection while using a VPN?",
        "hy am I mentally very lonely? How can I solve it?",
        "Which one dissolve in water quikly sugar, salt, methane and carbon di oxide?",
        "about me?",
    ]

    # vectorization of the raw_documents
    vectorizer = TfidfVectorizer(stop_words=None)
    X = vectorizer.fit_transform(raw_documents)

    words = vectorizer.get_feature_names()
    print("words", words)

    n_clusters = 9
    number_of_seeds_to_try = 10
    max_iter = 300
    number_of_process = 2  # seads are distributed
    # model = KMeans(n_clusters=n_clusters, max_iter=max_iter, n_init=number_of_seeds_to_try, n_jobs=number_of_process).fit(X)
    model = KMeans(
        n_clusters=n_clusters, max_iter=max_iter, n_init=number_of_seeds_to_try
    ).fit(X)
    print(model)

    labels = model.labels_
    # indices of preferible words in each cluster
    ordered_words = model.cluster_centers_.argsort()[:, ::-1]

    print("centers:", model.cluster_centers_)
    print("labels", labels)
    print("intertia:", model.inertia_)

    texts_per_cluster = numpy.zeros(n_clusters)
    for i_cluster in range(n_clusters):
        for label in labels:
            if label == i_cluster:
                texts_per_cluster[i_cluster] += 1

    print("Top words per cluster:")
    for i_cluster in range(n_clusters):
        print("Cluster:", i_cluster, "texts:", int(texts_per_cluster[i_cluster])),
        for term in ordered_words[i_cluster, :5]:
            print("\t" + words[term])

    print("\n")
    print("Prediction")

    text_to_predict = "Although both COVID-19 and influenza cause respiratory diseases, there are important differences between them and different modes of transmission"
    Y = vectorizer.transform([text_to_predict])
    predicted_cluster = model.predict(Y)[0]
    texts_per_cluster[predicted_cluster] += 1

    text = colored(
        "----- What is need to predict:------",
        "blue",
        attrs=["reverse", "blink"],
    )
    print(text)
    print(text_to_predict)
    print("#" * 20, "Prediction:", "#" * 20)
    print(
        "Cluster:",
        predicted_cluster,
        "texts:",
        int(texts_per_cluster[predicted_cluster]),
    ),
    for term in ordered_words[predicted_cluster, :5]:
        print("\t" + words[term])

    print("------------------------------")

    text_to_predict = "The mood of patients with new coronary pneumonia is still normal, and the hospital is operating normally"
    Y = vectorizer.transform([text_to_predict])
    predicted_cluster = model.predict(Y)[0]
    texts_per_cluster[predicted_cluster] += 1

    text = colored(
        "----- What is need to predict:------",
        "red",
        attrs=["reverse", "blink"],
    )
    print(text)

    print(text_to_predict)
    print("#" * 20, "Prediction:", "#" * 20)
    print(
        "Cluster:",
        predicted_cluster,
        "texts:",
        int(texts_per_cluster[predicted_cluster]),
    ),
    for term in ordered_words[predicted_cluster, :5]:
        print("\t" + words[term])
