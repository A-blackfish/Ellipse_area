## to get the interset points of two ellipse
import os
import math
from sympy import *
from Info_SecondElli import *

# define the angle of Fovea, here we only concider half of it.
Fovea = 7.5

def main():
	global Fovea
	Fovea = 7.5

	#x means helmet position, y means gaze point, here we did not concider timestamp
	x = np.array([100,0,100])  # pretending it as helmet position
	y = np.array([0,0,0])  # pretending it as gaze point
	
	x2 = np.array([0,100,100])
	y2 = np.array([0,0,0])
	norm_vec = np.array([0,0,1])  # norm vector of plane


	###--------------------------------------------------------------###
	#- we need a,b,a1,b1, the four values is constant
	#- beta, and coordinates, the two values is relative.
	#- we need the six values totally.
	
	a,b,s = get_area(x,y,norm_vec)
	a1,b1,s1 = get_area(x2,y2,norm_vec)
	
	c_x,c_y,m_1 = get_coordinate(x, y, x2, y2, norm_vec)
	c_x2,c_y2,m_2 = get_coordinate(x2, y2, x, y, norm_vec)
	# print(m_1,m_2)
	
	beta = Angle_bet_Ellipse(x, y, x2, y2, norm_vec)
	# beta2 = Angle_bet_Ellipse(x2, y2, x, y, norm_vec)
	print('beta:',beta)  # beta is the angle between two ellipse
	beta = get_angle4(beta)
	
	print('coordinates is:', c_x, c_y)
	print('a,b,a1,b1:',a,b,a1,b1)  # are the a,b of two ellipses respectively
	print('area of main ellipse: %f, and area of the second ellipse:%f' %(s, s1))
	
	
	# - testing example
	# a,b = 4,3  	# testing, define the a,b of main ellipse
	# a1,b1 = 3,2	# the a,b of the second ellipse
	# c_x = 3    	# testing, c_x, c_y is the center point of the second ellipse
	# c_y = 4	   	# testing
	# beta = np.pi/6
	
	s_main,s_rec = get_sec(a,b,a1,b1,c_x,c_y,beta)
	# print('s and s_rec:',s_main,s_rec)
	s_main2,s_rec2 = get_sec(a1,b1,a,b,c_x2,c_y2,np.pi-beta)
	# print('s_main2 and s_rec2:',s_main2,s_rec2)
	s_inter = s_main+s_main2-s_rec
	
	if s_main == -1:
		per_1 = s/s1 if (s/s1)<=1 else 1
		per_2 = s1/s if (s1/s)<=1 else 1
	else:
		per_1 = s_inter/s
		per_2 = s_inter/s1
		
	s_ave = (per_1+per_2)/2
	print('percentage of one is %f, of two is %f, average is %f' %(per_1,per_2,s_ave))
	
	os.system('pause')
	
	
def get_equ(a,b,beta):  # get the equation of the second ellipse
	A = (a**2)*((math.sin(beta))**2)+(b**2)*((math.cos(beta))**2)
	B = 2*(a+b)*(a-b)*math.sin(beta)*math.cos(beta)
	C = a**2*((math.cos(beta))**2)+b**2*((math.sin(beta))**2)
	f = a**2*b**2
	return A,B,C,f

def get_s1(a,b,theta):   # get the area of arc
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
	H = b-c
	theta = get_angle(L,H)
	L_length = get_length(L)
	H_length = get_length(H)
	# print('length of L,H:', L_length,H_length, 'theta:', theta)
	s = abs(L_length*H_length*math.sin(theta))/2
	# print('sub area:',s)
	return s
	
def dis_point(m):
	up = []
	down = []
	for i in range(4):
		if m[i][1]>0 and len(up)<2:
			up.append(m[i])
		else:
			down.append(m[i])
	return up,down
	
def get_arc_s(M,N,a,b):  # return small arc area 
	norm = np.array([1,0]) 
	theta = get_angle(M,norm)    #M,N are the intescting points
	beta = get_angle(N,norm)
	# print('theta, beta:', theta, beta,get_angle3(theta),get_angle3(beta))
	
	s1 = get_arc(a,b,theta,beta)  # get the area of the arc
	s2 = get_s2(M,N)		# get the area of the matrix
	s = s1-s2		# here is the area of intersection
	return s
	
def get_sec(a,b,a1,b1,c_x,c_y,gamma):  # To get the intersecting area of the main ellipse
	A,B,C,f = get_equ(a1,b1,gamma)  # testing, a,b,theta of the second ellipse.
	print ('A,B,C,f:',A,B,C,f)
	if (gamma%np.pi) == 0:
		return -1, -1
	
	x, y = symbols('x y')
	expr1 = (b**2)*(x**2)+(a**2)*(y**2)-(a**2)*(b**2)
	expr2 = A*(x-c_x)*(x-c_x)+C*(y-c_y)*(y-c_y)-B*(x-c_x)*(y-c_y)-f
	
	v = solve([expr1,expr2],[x,y],dtype=np.float32,minimal=True)  # get the cross point of two ellipses
	
	num_p = len(v)
	print('length of v:', num_p)
	print('the coordinates results:', v)
	# print('length of v(num of intersecting points):', num_p)
	
	###---------------------------###
	if num_p == 4:
		# print('there are four intersecting points here.')
		# print('v[0]:',v[0],'type of v[0]',type(v[0]))
		# print('type of v[0][0]', type(v[0][0]))
		M = [[0 for i in range(2)] for i in range(4)]
		for i in range(num_p):
			M[i][0] = re(v[i][0])
			M[i][1] = re(v[i][1])
		# print('only real part of v:',M)
		M = np.array(M, dtype=np.float32)
		s_rec = get_rectangle(M)  #the area of the center rectangle
		print('area of M:',s_rec)
		up,down = dis_point(M)
		print ('after judge:', up, down)
		
		s_arc_up = get_arc_s(up[0],up[1],a,b)
		s_arc_down = get_arc_s(down[0],down[1],a,b)
		s = s_rec+s_arc_up+s_arc_down
	###---------------------------###
	
	elif num_p == 2 or num_p == 3:
		M = v[0]		#M,N are the coordinates of the two cross point
		N = v[1]
		M = np.array(M,dtype=np.float32)
		N = np.array(N,dtype=np.float32)
		
		s = get_arc_s(M,N,a,b)
		
	elif num_p == 0 or num_p == 1:	
		s= 0
	
	return s, s_rec
	
if __name__ == '__main__':
	main()