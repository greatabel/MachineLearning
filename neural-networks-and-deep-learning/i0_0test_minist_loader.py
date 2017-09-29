import i2mnist_loader

def main():
    training_data, validation_data, test_data = i2mnist_loader.load_data()
    
def test_zip():
    a = [1,2,3,4]
    b = [5,6,7,8]
    c = zip(a,b)
    print(a,b,type(c),list(c))

if __name__ == "__main__":
    test_zip()
    main()