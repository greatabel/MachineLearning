import numpy as np
from i0load_ml100k import load

if __name__ == "__main__":
    data = load()
    data = np.transpose(data)
    # print(data[0:2])
    user1 = data[0]
    user2 = data[1]
    corr_between_user1_user2 = np.corrcoef(user1, user2)[0,1]
    print('corr_between_user1_user2=', corr_between_user1_user2)



