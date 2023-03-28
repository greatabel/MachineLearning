import numpy as np
from common import load_dataset
from d10network_evaluate import FNN_caller, show


def transform_to_range(arr):
    """
    同比例映射到0～150，标准还是100, 数组中最大值映射为150的上限，其他数同比例映射
    """
    denominator = len(arr)
    maxElement = np.amax(arr)
    radio = maxElement / 150
    newArr = arr / radio
    numerator = (newArr > 100).sum()
    r = numerator / denominator
    if r > 0.2:
        return False
    else:
        return True


def main():
    input_lines, n_sentences, p_sentences = load_dataset()
    positive = transform_to_range(input_lines)
    print("sentiment=", positive)
    db = None
    if positive:
        db = p_sentences
    else:
        db = n_sentences
    index = FNN_caller(input_lines)
    print(show("Plants start saying:"), "#" * 20)
    print(db[index])
    print(show("Plants finished saying:"), "#" * 20)


if __name__ == "__main__":
    main()
