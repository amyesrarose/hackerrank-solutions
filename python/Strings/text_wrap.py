"""
Problem :Text Wrap
Link : https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true
Task 
You are given a string  and width .
Your task is to wrap the string into a paragraph of width .

Function Description

Complete the wrap function in the editor below.

wrap has the following parameters:

string string: a long string
int max_width: the width to wrap to
Returns

string: a single string with newline characters ('\n') where the breaks should be
Input Format

The first line contains a string, .
The second line contains the width, .

Constraints
0<= len(string)<=1000
0<= max_width <= len(string)

Sample Input 
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4

Sample Output 
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ

"""

import textwrap # text warp need to be imported to use

def wrap(string,max_width): #defining wrap method with 2 parameter
    return textwrap.fill(string, max_width) # textwrap Wraps text and joins lines with \n ("\n".join(wrap(...))).

if __name__ == '__main__': 
    string,max_width = input(), int(input())
    result = wrap(string,max_width)
    print(result)





"""
This version of solution is without using textwrap build in method

def wrap(string,max_width):
    result = [string[i:i+max_width] for i in range(0,len(string),max_width)
              ]
    return result
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string,max_width)
    print(*result,sep="\n")
"""