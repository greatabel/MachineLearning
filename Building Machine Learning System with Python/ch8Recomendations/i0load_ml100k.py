def load():
    '''Load ML-100k data

    Returns the review matrix as a numpy array'''
    import numpy as np
    from scipy import sparse
    from os import path

    if not path.exists('data/ml-100k/u.data'):
        raise IOError("Data has not been downloaded.\nTry the following:\n\n\tcd data\n\t./download.sh")

    # The input is in the form of a CSC sparse matrix, so it's a natural fit to
    # load the data, but we then convert to a more traditional array before
    # returning
    data = np.loadtxt('data/ml-100k/u.data')
    ij = data[:, :2]
    ij -= 1  # original data is in 1-based system
    values = data[:, 2]
    reviews = sparse.csc_matrix((values, ij.T)).astype(float)
    return reviews.toarray()

if __name__ == "__main__":
    rvs = load()
    print(len(rvs), rvs[0:5])