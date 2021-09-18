from numpy import loadtxt


def load_dataset():
    input_lines = loadtxt(
        "data/input_demo.txt", comments="#", delimiter="\n", unpack=False
    )
    n_sentences, p_sentences = None, None
    n_path = "data/sentences_source_n.txt"

    with open(n_path) as file:
        n_sentences = file.readlines()
        n_sentences = [line.rstrip() for line in n_sentences]

    p_path = "data/sentences_source_p.txt"

    with open(p_path) as file:
        p_sentences = file.readlines()
        p_sentences = [line.rstrip() for line in p_sentences]

    return input_lines, n_sentences, p_sentences
