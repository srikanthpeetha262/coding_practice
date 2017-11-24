'''
######################################################################
Author: Srikanth Peetha
Date: 11-24-2017
About: Python practice questions from the web

Task: Rotate matrix (90 degress, clockwise)
######################################################################


QUESTION:
You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).

Example

For

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
the output should be

rotateImage(a) =
    [[7, 4, 1],
     [8, 5, 2],
     [9, 6, 3]]
Input/Output

[time limit] 4000ms (py)
[input] array.array.integer a

Guaranteed constraints:
1 ≤ a.length ≤ 100,
a[i].length = a.length,
1 ≤ a[i][j] ≤ 104.

[output] array.array.integer
'''

# ~~~~~~~~~~~ Solution ~~~~~~~~~~~
import copy

#function to display the matrix on the screen
def display(matrix,string):
	print "\n" + string
	for i in xrange(len(matrix)):
		print matrix[i]


# Function to rotate the matrix
def rotation(a):
	b = copy.deepcopy(a)
	lim = len(a)

	for i in range(0,lim):
		p = (lim-1) - i
		for j in range(0,lim):
			b[j][i] =  copy.deepcopy(a[p][j])	
	str2="After 90 deg in clock-wise, the rotated matrix is"
	display(b,str2)


# Main function
def main():
	arr = [[1,2,3],[4,5,6], [7,8,9]]
	#arr = [[1]]
	str1 = "The original Matrix is"
	display(arr,str1)
	rotation(arr)

main()
