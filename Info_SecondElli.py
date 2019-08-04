###--- July 2 --###
###--- Danny Duan --###
###--- python to get the cooridinate, a,b and beta ---###
###--- give gaze point x([]), and pos point y([]), norm vecort of the plane, ---###
###--- this function will return the angle between the two ellipse, and the coordinate 
###--- of the center point of the second ellipse ---###
import os
import math
import numpy as np
from trigonometric import *
from IntersectPoint_main import Fovea

def main():
	# print the length and angle of two vectors
	x = np.array([1,0,1])  # pretending it as position
	y = np.array([0,0,0])  # pretending it as gaze point
	x2 = np.array([0,-1,1])
	y2 = np.array([0,0,0])
	norm_vec = np.array([0,0,1])  # norm vector of the plane
	
	# NP1 = Angle_ellipse(x, y, norm_vec)
	# NP2 = Angle_ellipse(x2, y2, norm_vec)
	# print(NP1, NP2)
	# a, b = get_ab(x, y, norm_vec)
	# print ('a,b', a, b)
	gamma = Angle_bet_Ellipse(x, y, x2, y2, norm_vec)
	print('angle between vector1 and vector2:', gamma)
	x,y = get_coordinate(x, y, x2, y2, norm_vec)
	print('coordinates is:', x, y)

	os.system('pause')

def Angle_ellipse(x, y, norm): # get the vertical vector of norm_vec
	P1 = x-y
	length = get_length(P1)*abs(math.cos(get_angle(P1,norm)))
	# print ('length:', length,'cos:', abs(math.cos(get_angle(P1,norm))))
	P1_N = norm*length
	NP1 = -P1+P1_N
	return NP1

def Angle_bet_Ellipse(x, y, x2, y2, norm):  # get the projection angle between two vectors
	NP1 = Angle_ellipse(x, y, norm)
	NP2 = Angle_ellipse(x2, y2, norm) 
	return get_angle2(NP1, NP2)
	
def get_ab(x,y,norm):  # get a,b of the ellipse, x is the pos position, y is gaze point, norm is the norm vector of the plane
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
		return a, b
	except:
		print('Input error! The angle between norm_vec and observer vecort is belong (0, pi/2), check it!!! ')
		return -1,-1
	
def get_m(x, y, norm):  #m is the x coordinate of the second ellipse
	L = get_length(x-y)  # length of the observing vector
	# print('L',L)
	
	alpha = get_angle4(Fovea)# The number here is the angle of fovea. the angle is 1 and transfer it to radian 
	
	obe_v = x - y  # obe_v is the vetor of observer
	beta = get_angle(obe_v,norm)  # beta is the angle between obe_v and norm vector of plane
	# print('angle with the norm vector', get_angle3(beta))
	
	a = (L*math.sin(beta)-L*math.cos(beta)*math.tan(beta-alpha)+
		(L*math.cos(beta)/math.tan(np.pi/2-beta-alpha)-L*math.sin(beta)))/2  # a is one parameter of ellipse equation  
	
	m = a-(L*math.sin(beta)-L*math.cos(beta)*math.tan(beta-alpha)) # the x coordinate of one point on ellipse

	return m

def get_coordinate(x, y, x2, y2, norm):  #get the relatively cooridinate of an ellipse.###-----------------------------------###
	L = get_m(x, y, norm)		# x, y is the main ellipse and x2, y2 is a sloping ellipse
	m = get_m(x2, y2, norm)

	beta = Angle_bet_Ellipse(x, y, x2, y2, norm)
	beta = get_angle4(beta)
	# print ('L, m, beta:', L,m,beta)
	
	x = L + m*math.cos(beta+np.pi)
	y = m*abs(math.sin(beta))
	return x, y, L
	
if __name__=='__main__':
	main()

