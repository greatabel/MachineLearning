from collections import defaultdict

import i2mnist_loader

def main():
    training_data, validation_data, test_data = i2mnist_loader.load_data()
    print(training_data.shape, validation_data.shape, test_data.shape)
    return ""

def avg_darkness(training_data):
    return ""

def guess_digit(image, avgs):
    return ""

if __name__ == "__main__":
    main()