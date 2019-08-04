###--- July 2 --###
###--- Danny Duan --###
###--- python trigonometric function ---###
###--- give gaze point x([]), and pos point y([]), norm vecort of the plane, ---###
###--- this function will return the corresponding a,b,s(area of the ellipse) of the formed ellipse ---###
import os
import math
import numpy as np
from IntersectPoint_main import Fovea
def main():
	# print the length and angle of two vectors
	x = np.array([1,0,1])  # pretending it as position
	y = np.array([0,0,0])  # pretending it as gaze point
	x2 = np.array([2,2,0])
	y2 = np.array([0,0,0])
	norm_vec = np.array([0,0,1])  # norm vector of the plane
	
	# print ('s equel to', np.pi*math.tan(get_angle4(1))*math.tan(get_angle4(1)))
	
	s1, a, b = get_area(x,y,norm_vec)
	# print (s1, a, b)
	s2, a1, b1 = get_area(x2,y2,norm_vec)
	print ('s1=%f , s2=%f' %(s1,s2), 'a,b,a1,b1:',a,b,a1,b1)

	os.system('pause')

def get_length(x):
	return np.sqrt(x.dot(x))

def get_cos(x,y):
	return x.dot(y)/(get_length(x)*get_length(y))

def get_angle(x,y):   # get the radian of two vectors
	return np.arccos(get_cos(x,y))

def get_angle2(x,y):  # get the angle of two angles
	return get_angle(x,y)*360/(2*np.pi)

def get_angle3(x):   # transfer radian to angle
	return x*180/np.pi
	
def get_angle4(x):  # transfer angle to radian
	return x*np.pi/180
	
def get_area(x,y,norm):  # x is the pos position, y is gaze point, norm is the norm vector of the plane
	L = get_length(x-y)  # length of the observing vector
	
	alpha = get_angle4(Fovea)# alpha is the angle of fovea. the angle is 1 and transfer it to radian 
	
	obe_v = x - y  # obe_v is the vetor of observer
	beta = get_angle(obe_v,norm)  # beta is the angle between obe_v and norm vector of plane
	# print('angle between norm and observer:', beta, get_angle3(beta))
	
	try:
		a = (L*math.sin(beta)-L*math.cos(beta)*math.tan(beta-alpha)+
		(L*math.cos(beta)/math.tan(np.pi/2-beta-alpha)-L*math.sin(beta)))/2  # a is one parameter of ellipse equation 
		
		m = a-(L*math.sin(beta)-L*math.cos(beta)*math.tan(beta-alpha)) # the x coordinate of one point on ellipse
		n = L*math.tan(alpha) # the y coordinate of one point on ellipse. m,n represent one point on the ellipse
		b = a*n/math.sqrt((a+m)*(a-m))
		s = np.pi*a*b  # the area of the projection ellipse, s=pi*a*b
		return a, b, s
	except:
		print('Input error! The angle between norm_vec and observer vecort is belong (0, pi/2), check it!!! ')
		return -1,-1,-1


if __name__=='__main__':
	main()

