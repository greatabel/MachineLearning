import numpy as np
from common import load_dataset
from d10network_evaluate import FNN_caller, show

import wave
import argparse
import time

# 读取狗狗音频，并且进行数字化转换
def read_wav_file(file_path):
    with wave.open(file_path, "r") as wav_file:
        n_channels, sampwidth, framerate, n_frames = wav_file.getparams()[:4]
        data = wav_file.readframes(n_frames)
        audio_data = np.frombuffer(data, dtype=np.dtype(f"<i{sampwidth}"))

        if n_channels > 1:
            audio_data = audio_data.reshape(-1, n_channels)

    return audio_data


def transform_to_range(arr):
    """
    数据压缩：
    同比例映射到0～150，标准还是100,
    数组中最大值映射为150的上限，其他数同比例映射
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
    parser = argparse.ArgumentParser(description="Read a WAV file of dogs")
    parser.add_argument(
        "file_path",
        metavar="FILE_PATH",
        type=str,
        help="Path to the WAV file.",
        default="dog0.wav",
    )
    args = parser.parse_args()
    # python i0dog_speak.py dog0.wav
    print("args.file_path=", args.file_path)
    time.sleep(1)
    # 读取 wav 文件并将其映射为 Python 数组
    audio_data = read_wav_file(args.file_path)
    print(audio_data)

    print("-" * 20)
    input_lines, n_sentences, p_sentences = load_dataset()
    positive = transform_to_range(audio_data)
    print("sentiment=", positive)
    db = None
    if positive:
        db = p_sentences
    else:
        db = n_sentences
    index = FNN_caller(input_lines)

    print("\n")
    time.sleep(1)
    print(show("Dogs start saying:   "), "#" * 20)
    print(db[index])
    print(show("Dogs finished saying:"), "#" * 20)


if __name__ == "__main__":
    main()
