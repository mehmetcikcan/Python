#-*- coding:utf-8 -*-
from math import exp
import numpy as np

class perceptron():
	
	def inputs(self):

		self.satirx = 1
		self.sutunx = 0
		self.matrisx = []

		while(True):

			print 'X',self.sutunx,' elemanini giriniz yada cikis icin q ya basiniz: '
			sayi = raw_input ()
			
			
			if (sayi == 'q'):
				print 'olusan matris'

				for self.sutunx in range(self.sutunx):
					print self.matrisx[self.sutunx]

				break

			else:
				
				self.matrisx += [sayi]
				print(self.matrisx)
				self.sutunx = self.sutunx+1
				

	def theta(self):

		self.satirt = 1
		self.sutunt = 0
		self.matrist = []

		while(True):

			print 'T',self.sutunt,' elemanini giriniz yada cikis icin q ya basiniz: '
			sayi = raw_input ()
			
			
			if (sayi == 'q'):
				print 'olusan matris'

				for self.sutunt in range(self.sutunt):
					print self.matrist[self.sutunt]

				break

			else:
				
				self.matrist += [sayi]
				print(self.matrist)
				self.sutunt = self.sutunt+1

	def general_activation_function(self,x,t,sx,st):

		bias = int(raw_input('Bias giriniz: '))
		z = 0
		for sx in range(sx+1):
					#print t[st]
					z = z+(int(x[sx])*int(t[sx]))
		z = z+bias

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

	result=f_p.general_activation_function(f_p.matrisx,f_p.matrist,f_p.sutunx,f_p.sutunt)
	
	print 'Sonuc: ', result
