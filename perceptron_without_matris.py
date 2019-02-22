# Python# encoding=utf8
from numpy.random import random_sample
from math import exp
import numpy as np

class perceptron():
	
	def inputs(self):
	
		self.x1=input('Input X1: ')
		print 'X1 degeri',self.x1, 'ayarlandi. \n'

		self.x2=input('Input X2: ')
		print 'X2 degeri', self.x2, 'ayarlandi. \n'

		self.x3=input('Input X3: ')
		print 'X3 degeri', self.x3, 'ayarlandi. \n'
	
		self.bias=input('Input Bias: ')
		print 'Bias degeri', self.bias, 'ayarlandi. \n'



	
	def theta(self):

		self.T0=input('Input θ0: ')
		print 'T0 degeri',self.T0, 'ayarlandi. \n'

		self.T1=input('Input θ1: ')
		print 'T1 degeri',self.T1, 'ayarlandi. \n'

		self.T2=input('Input θ2: ')
		print 'T2 degeri', self.T2, 'ayarlandi. \n'

		self.T3=input('Input θ3: ')
		print 'T3 degeri', self.T3, 'ayarlandi. \n'

	def general_activation_function(self, a1, b1, a2, b2, a3, b3, bs, bt):

		z=(a1*b1)+(a2*b2)+(a3*b3) + bs*bt

		print 'Aktivasyon fonksiyonunu seciniz.\n'
		print 's = sigmoid,  h = hyperbolic tangent,  r=rectified lineer unit.\n'
		func=raw_input('Seciminizi yapiniz: ')

		if (func == 's'):
			return 1/(1+np.exp(-z)) #sigmoid

		elif (func == 'h'):
			return (np.exp(z) - np.exp(-z))/(np.exp(z) + np.exp(-z)) #hyperblic_tangent

		elif (func == 'r'):
			return max(0, z) #rectified_lineear_unit



if __name__ == '__main__':
	f_p = perceptron()
	f_p.inputs()
	f_p.theta()

	result=f_p.general_activation_function(f_p.x1, f_p.T1, f_p.x2, f_p.T2, f_p.x3, f_p.T3, f_p.bias, f_p.T0)
	
	print 'Sonuc: ', result
