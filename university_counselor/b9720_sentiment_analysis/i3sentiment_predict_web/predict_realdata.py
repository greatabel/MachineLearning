import numpy as np


from tensorflow.keras import models
import tensorflow as tf 

import pickle




def flow_predict(i):
	i = int(i)
	print("i=", i)
	MyX_test_oh = None
	# identical to the previous one
	mymodel = tf.keras.models.load_model('drop_model.h5')
	with open('test.pkl','rb') as f:
	     MyX_test_oh = pickle.load(f)  

	# 真实数据预测
	q = mymodel.predict( np.array( [MyX_test_oh[i],] )  )
	result = np.around(q,decimals=3)
	return result

if __name__ == "__main__":
	flow_predict(["Tuesday", "13:35", "placeid0", "down"])