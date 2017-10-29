from  d6mean_squared_error import mse, generate_test_data
from termcolor import colored

def batch(l, batch_size):
    n = len(l)
    # print('n =>', n, 'l =>', l)
    mini_batches = [
        l[k:k+batch_size]
        for k in range(0, n, batch_size)
    ]
    # print('mini_batches =>', mini_batches)
    return mini_batches

def main():
    a = 2
    b = 3
    noise = a / 10.0
    # 2.5e2 = 2.5 x 102 = 250
    for scope in [10, 100, 1000, int(1e4), int(1e5), int(1e6)]:
        print(colored('scope =>', 'blue'), scope )
        data_size = scope
        # print('noise=>', noise)
        x, y_pred = generate_test_data(a + noise, b + noise, data_size)
        y = a * x + b
        all_mse = mse(y, y_pred)
        print(colored(' mse(y, y_pred) =>', 'red'), all_mse )
        batch_size = data_size // 5

        y_group = batch(y, batch_size)
        y_pred_group = batch(y_pred, batch_size)
        for i in range(len(y_group)):
            batch_mse = mse(y_group[i], y_pred_group[i])
            print(colored(' batch_mse[' + str(i) + '] =>', 'red'), 
                    batch_mse, "{0:.0f}%".format(100 * abs(batch_mse - all_mse)/ all_mse))

if __name__ == "__main__":
    main()