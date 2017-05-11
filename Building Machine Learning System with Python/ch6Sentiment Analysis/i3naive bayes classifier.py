from sklearn.naive_bayes import GaussianNB
import numpy as np


# https://www.analyticsvidhya.com/blog/2015/09/naive-bayes-explained/
def main():
    #assigning predictor and target variables
    X = np.array([[-3,7],[1,5], [1,2], [-2,0],
     [2,3], [-4,0], [-1,1], [1,1], [-2,2], [2,7], [-4,1], [-2,7]])
    Y = np.array([3, 3, 3, 3, 4, 3, 3, 4, 3, 4, 4, 4])

    # Create a Gaussian classifer
    model = GaussianNB()

    # Train the model using the trainning sets
    model.fit(X, Y)

    # Predict Outupt
    target = [ [1,2], [3,4] ]
    predicted = model.predict(target)
    predict_proba = model.predict_proba(target)

    print(predicted)
    print('-'*20)
    print(predict_proba)


if __name__ == '__main__':
    main()