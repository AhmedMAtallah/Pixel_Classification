'''
ECE276A WI21 PR1: Color Classification and Recycling Bin Detection
'''


import numpy as np
from generate_rgb_data import read_pixels

class PixelClassifier():
  def __init__(self):
    '''
	    Initilize your classifier with any parameters and attributes you need
    '''
    pass


  def classify(self,X):
    '''
	    Classify a set of pixels into red, green, or blue
	    
	    Inputs:
	      X: n x 3 matrix of RGB values
	    Outputs:
	      y: n x 1 vector of with {1,2,3} values corresponding to {red, green, blue}, respectively
    '''
    n = len(X)

    y = np.zeros((n,1))
    WR = [13.4443588081522289457, -9.2833342191806078603, -8.9677301661786081866]
    #WG = [-10.5310142417393599601,  14.4472322584629910835,  -9.3877015214741206250]
    WG= [-10.531014241740744, 14.447232258464899, -9.387701521475329]
    WB = [-10.6297631459127899234,  -9.5226131194892715826,  14.5089754156606929314 ]
    # YOUR CODE HERE
    # Just a random classifier for now
    # Replace this with your own approach 
    for i in range (n):
      xi = X[i][:]
      dr = np.dot(xi,WR)
      dg = np.dot(xi,WG)
      db = np.dot(xi,WB)

      if dr > 0:
        y[i] = 1
      
      if dg > 0 :
        y[i] = 2
      
      if db > 0:
        y[i] = 3

    
    return y

