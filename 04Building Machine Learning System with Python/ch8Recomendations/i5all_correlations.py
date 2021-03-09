import numpy as np


def all_correlations(y, X):
    from scipy import spatial
    y = np.atleast_2d(y)
    # print('y=', y)
    sp = spatial.distance.cdist(X, y, 'correlation')
    # print('sp=', sp)
    # The "correlation distance" is 1 - corr(x,y); so we invert that to obtain the correlation
    return 1 - sp.ravel()

def all_correlations_book_version(bait, target):
    '''
    corrs = all_correlations(bait, target)

    corrs[i] is the correlation between bait and target[i]
    '''
    return np.array(
        [np.corrcoef(bait, c)[0, 1]
         for c in target])
    
def all_correlations_fast_no_scipy(y, X):
    '''
    Cs = all_correlations(y, X)

    Cs[i] = np.corrcoef(y, X[i])[0,1]
    '''
    X = np.asanyarray(X, float)
    y = np.asanyarray(y, float)
    xy = np.dot(X, y)
    y_ = y.mean()
    ys_ = y.std()
    x_ = X.mean(1)
    xs_ = X.std(1)
    n = float(len(y))
    ys_ += 1e-5  # Handle zeros in ys
    xs_ += 1e-5  # Handle zeros in x

    return (xy - x_ * y_ * n) / n / xs_ / ys_

if __name__ == "__main__":
    a = np.array([[0, 0, 0],
                  [0, 0, 1],
                  [0, 1, 0],
                  [0, 1, 1],
                  [1, 0, 0],
                  [1, 0, 1],
                  [1, 1, 0],
                  [1, 1, 1]])
    b = np.array([[ 0.1,  0.2,  0.4]])
    result = all_correlations(b, a)
    print('1 #'*10, result)
    result = all_correlations_book_version(b, a)
    print('2 #'*10, result)