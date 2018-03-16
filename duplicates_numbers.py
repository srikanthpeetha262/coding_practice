'''
######################################################################
Author: Srikanth Peetha; [@srikanthpeetha262]
Date: 3-16-2018
About: Python practice questions from the web

Task: Duplicate Numbers
######################################################################


QUESTION:
Assuming each number repeats itself only once, find the second repeating number in the given list
'''

def func1():

	a =[2,3,3,1,5,2]
	d={}  #define a dictonary
	out = 0
	print a

	for i in a:
		
		if (i in d):
			out += 1
			if (out ==2):
				return i
		else:
			d[i] = i

	return 0

    
if __name__ == '__main__':
	out = func1()
	if out==0:
		print "no match found"
	else:
		print "Second Duplicate(a) = ", out

