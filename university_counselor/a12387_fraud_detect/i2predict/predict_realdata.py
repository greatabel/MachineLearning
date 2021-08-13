#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import sklearn.preprocessing as sp
import sklearn.model_selection as ms
import sklearn.svm as svm
import sklearn.metrics as sm
import sklearn.naive_bayes as nb

import pickle
from predict_train import MyEncoder
from process_phone_with_transaction import load_obj

filename = "model_file_name.pkl"

# load the model from disk
# loaded_model = pickle.load(open(filename, 'r'))
# encoders = pickle.load(open('myencoders.pkl', 'rb'))


def flow_predict(i):
	'''
	get deviceid or phonenumber 's fraud or not-fraud status
	based on machine learing training results
	'''
	k_v = load_obj("k_v")
	print(k_v, "#" * 20)
	r = k_v[i]
	return int(r)


if __name__ == "__main__":
    flow_predict(["Tuesday", "13:35", "placeid0", "down"])
