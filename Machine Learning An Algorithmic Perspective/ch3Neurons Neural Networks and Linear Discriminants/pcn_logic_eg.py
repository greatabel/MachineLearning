#!/usr/bin/env python
# -*- coding: utf8 -*-
"""Page 30-32, Perceptron algorithm,

with an OR logic demo, predict it's outputs and calculate it's Confusion matrix
"""
# Code from Chapter 2 of Machine Learning: An Algorithmic Perspective
# by Stephen Marsland
# (http://seat.massey.ac.nz/personal/s.r.marsland/MLBook.html)

# You are free to use, change, or redistribute the code in any way you wish for
# non-commercial purposes, but please maintain the name of the original author.
# This code comes with no warranty of any kind.

# Stephen Marsland, 2008
import numpy as np

class pcn(object):
    """ A basic Perceptron (the same pcn.py except with the weights printed
    and it does not reorder the inputs)"""

    def __init__(self,inputs,targets):
        """ Constructor """
        # Set up network size
        #if ndim(inputs)>1:
            #self.nIn = shape(inputs)[1]
        #else:
            #self.nIn = 1

        #if ndim(targets)>1:
            #self.nOut = shape(targets)[1]
        #else:
            #self.nOut = 1
        self.nIn = inputs.shape[1] if inputs.ndim > 1 else 1
        self.nOut = targets.shape[1] if targets.ndim > 1 else 1

        self.nData = inputs.shape[0]

        # Initialise network
        self.weights = np.random.rand(self.nIn+1,self.nOut) * 0.1 - 0.05
        # self.weights = np.zeros((self.nIn+1,self.nOut))

    def pcntrain(self,inputs,targets,eta,nIterations):
        """ Train the thing """
        # Add the inputs that match the bias node
        inputs = np.concatenate((inputs,-np.ones((self.nData,1))),axis=1)

        # Training
        for n in range(nIterations):

            self.outputs = self.pcnfwd(inputs);
            self.weights += eta*np.dot(inputs.transpose(), targets-self.outputs)
            print( "Iteration: ", n)
            print( self.weights)

            activations = self.pcnfwd(inputs)
        print("Final outputs are:")
        print( activations )
        #return self.weights

    def pcnfwd(self,inputs):
        """ Run the network forward """

        outputs = np.dot(inputs,self.weights)

        # Threshold the outputs
        return np.where(outputs>0,1,0)


    def confmat(self,inputs,targets):
        """Confusion matrix"""

        # Add the inputs that match the bias node
        inputs_bias = np.concatenate((inputs,-np.ones((self.nData,1))),axis=1)
        outputs = np.dot(inputs_bias, self.weights)

        nClasses = targets.shape[1]

        if nClasses==1:
            nClasses = 2
            outputs = np.where(outputs>0,1,0)
        else:
            # 1-of-N encoding
            outputs = np.argmax(outputs,1)
            targets = np.argmax(targets,1)

        cm = np.zeros((nClasses,nClasses))
        for i in range(nClasses):
            for j in range(nClasses):
                cm[i,j] = np.sum(np.where(outputs==i,1,0) *
                                 np.where(targets==j,1,0))

        print(cm)
        print(np.trace(cm)/np.sum(cm))
def xor_logic(is3d=False):
    """ Run XOR logic functions """
    if is3d:
        inputs = np.array([[0,0,1],[0,1,0],[1,0,0],[1,1,0]])
    else:
        inputs = np.array([[0,0],[0,1],[1,0],[1,1]])
    targets = np.array([[0],[1],[1],[0]])
    p = pcn(inputs, targets)
    p.pcntrain(inputs, targets, .25, 15)
    # predict it's outputs
    inputs_bias = np.concatenate((inputs, -np.ones((inputs.shape[0],1))),
                                 axis=1)
    print(p.pcnfwd(inputs_bias))
    # calculate it's Confusion matrix
    p.confmat(inputs, targets)
    
def main():
    """ Run OR logic functions """
    inputs = np.array([[0,0],[0,1],[1,0],[1,1]])
    targets = np.array([[0],[1],[1],[1]])
    p = pcn(inputs, targets)
    p.pcntrain(inputs, targets, .25, 6)
    # predict it's outputs
    inputs_bias = np.concatenate((inputs, -np.ones((inputs.shape[0],1))),
                                 axis=1)
    print(p.pcnfwd(inputs_bias))
    # calculate it's Confusion matrix
    p.confmat(inputs, targets)

    # Run XOR logic functions
    xor_logic()

    # Run XOR logic functions, 3D version
    xor_logic(is3d=True)
if __name__ == "__main__":
    main() 