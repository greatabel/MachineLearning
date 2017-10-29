from  d6mean_squared_error import mse, generate_test_data
from termcolor import colored


def main():
    a = 2
    b = 10
    noise = a / 10.0    
    x, y_pred = generate_test_data(a + noise, b + noise, 100)
    y = a * x + b
    

    print(colored(' mse(y, y_pred) =>', 'red'), mse(y, y_pred))

if __name__ == "__main__":
    main()