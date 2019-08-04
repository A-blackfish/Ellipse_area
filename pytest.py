###--- July 2 ---###
###--- Danny Duan ---###


import os
import math
import numpy as np
from sympy import *
from sympy.parsing.sympy_parser import parse_expr 
from trigonometric import *

def main():
	M = [[i for i in range(2)] for i in range(4)] 
	M[0] = [3,3]
	M[1] = [-3,3]
	M[2] = [3,-2]
	M[3] = [-3,-6]
		
	s = get_rectangle(M)
	print('area of the rectangle is:%f' %(s))
	print('M:',M)
	dis_point(M)
	plot_implicit(parse_expr('x**2+y**2-5'))
	os.system('pause')

def get_s1(a,b,theta):
	s_arc1 = 0.5*a*b
	mid = math.atan(((b-a)*math.sin(2*theta))/(b+a+(b-a)*(math.cos(2*theta))))
	s_arc2 = theta - mid
	s_arc = s_arc1*s_arc2
	return s_arc

def get_arc(a,b,theta,beta):  # get the area of arc
	s_theta = get_s1(a,b,theta)
	s_beta = get_s1(a,b,beta)
	s_arc = abs(s_theta-s_beta)
	return s_arc

def get_s2(M,N):  # get the area of the matrix
	return 0.5*abs(M[0]*N[1]-M[1]*N[0])

def get_rectangle(M):  # get the area of 4 points intersection, the rectangle is consisted of 4 triangle
	a = M[0]
	b = M[1]
	c = M[2]
	d = M[3]
	area_tr1 = area_triangle(a,b,c)
	area_tr2 = area_triangle(a,b,d)
	area_tr3 = area_triangle(a,c,d)
	area_tr4 = area_triangle(b,c,d)
	s = area_tr1+area_tr2+area_tr3+area_tr4
	return s/2

def area_triangle(a,b,c):    #get the area of triangle. coordinates of three points
	a = np.array(a)
	b = np.array(b)
	c = np.array(c)
	L = a-b
	H = c-b
	theta = get_angle(L,H)
	L_length = get_length(L)
	H_length = get_length(H)
	# print('length of L,H:', L_length,H_length, 'theta:', get_angle3(theta))
	s = abs(L_length*H_length*math.sin(theta))/2
	# print('sub area:',s,'a,b,c:',a,b,c)
	return s
	
def dis_point(m):
	up = []
	down = []
	for i in range(4):
		if m[i][1]>0:
			up.append(m[i])
		else:
			down.append(m[i])
	print ('after judge:', up, down)
	
if __name__ == '__main__':
	main()