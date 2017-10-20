import numpy as np
from termcolor import colored

questions = ['whether is fine?', 'Boy friend or girl friend with you?',
             'Place is near your location?']
def single_perceptron(x):
    # print('-' * 20 )
    # x = [10, 20, 30, 40, 50]

    w = np.random.rand(1,3)
    threshold = 1
    output = None
    # print('w ->', w, w.shape)
    w = w.T
    print('w (importance or weight)->', w, w.shape)
    isum = np.dot(x, w)
    print('sum=', isum)

    if isum <= threshold:
        output = 0
    else:
        output = 1
    print(output)



def main():
    for i in range(5):
        print(colored('i =>','red'), i)
        x = np.random.randint(2, size=3)
        for j in zip(questions, x):
            print(j[0],"->", "Yes" if j[1] == 1 else "No")
        single_perceptron(x)


if __name__ == "__main__":
    main()