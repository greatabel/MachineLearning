import i2mnist_loader

from sklearn import svm
import time

def svm_baseline():
    training_data, validation_data, test_data = i2mnist_loader.load_data()

    clf = svm.SVC()
    clf.fit(training_data[0], training_data[1])

    predictions = [int(a) for a in clf.predict(test_data[0])]
    num_correct = sum(int(a == y) for a, y in zip(predictions, test_data[1]))
    print("Baseline classifier using an SVM.")
    print("%s of %s values correct." % (num_correct, len(test_data[1])) )

# result:
# Baseline classifier using an SVM.
# 9435 of 10000 values correct.
if __name__ == "__main__":
    tic = time.clock()
    svm_baseline()
    toc = time.clock()
    print("time=",toc - tic)