from collections import defaultdict

import i2mnist_loader

def main():
    training_data, validation_data, test_data = i2mnist_loader.load_data()
    avgs = avg_darkness(training_data)
    print(avgs)
    return ""

def avg_darkness(training_data):
    digit_counts = defaultdict(int)
    darknesses = defaultdict(float)
    for image, digit in zip(training_data[0], training_data[1]):
        digit_counts[digit] += 1
        darknesses[digit] += sum(image)
    avgs = defaultdict(float)
    for digit, n in digit_counts.items():
        avgs[digit] = darknesses[digit] / n
    return avgs

def guess_digit(image, avgs):
    return ""

if __name__ == "__main__":
    main()