
'''
######################################################################
Author: Srikanth Peetha
Date: 11-24-2017
About: Python practice questions from the web

Task: Pascal triangle
######################################################################
QUESTION: Write a program to print pascal triangle

Output:

1
1 1
1 2 1
1 3 3 1
1 3 4 3 1
1 5 10 10 5 1
1 6 15 20 15 6 1
... and so on....

'''

n = input("enter the number of lines you wanna print: ")
pas = []
temp = []

line = 1
while (line <= n):
	#print pas
	#print temp
	del temp[:]
	i = 1
	
	while(i <= line):
		if( i==1 or i==line ):
			temp.append(1)		
		else:
			temp.append(pas[i-1] + pas[i-2])
		i += 1
	del pas[:]
	

	for a in range(0, len(temp)):
		pas.append(temp[a])

	print pas
	
	line += 1


	
