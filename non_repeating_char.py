'''
######################################################################
Author: Srikanth Peetha; [@srikanthpeetha262]
Date: 11-24-2017
About: Python practice questions from the web

Task: First non-repeating character
######################################################################


QUESTION:

Note: Write a solution that only iterates over the string once and uses O(1) additional memory.

Given a string s, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.

Example

For s = "abacabad", the output should be
firstNotRepeatingCharacter(s) = 'c'.

There are 2 non-repeating characters in the string: 'c' and 'd'. Return c since it appears in the string first.

For s = "abacabaabacaba", the output should be
firstNotRepeatingCharacter(s) = '_'.

There are no characters in this string that do not repeat.

Input/Output

[time limit] 4000ms (py)
[input] string s

A string that contains only lowercase English letters.

Guaranteed constraints:
1 <= s.length <= 105.

[output] char

The first non-repeating character in s, or '_' if there are no characters that do not repeat.
'''

# ~~~~~~~~~~~ Solution ~~~~~~~~~~~~~~~~
def firstNotRepeatingCharacter(s):
	check = 0
	d = {}
	
	for i in s:
		if i in d:
			d[i] += 1
		else:
			d[i] = 0
	print d
	
	for i in s:
		if d[i] == 0:
			check = 1
			return i
		
	if check == 0:
		return 22
	

def main():
	# case 1
	print firstNotRepeatingCharacter('xdnxxlvupzuwgigeqjggosgljuhliybkjpibyatofcjbfxwtalc')

	# case 2
	print firstNotRepeatingCharacter('tomatto')

main()

