
"""This module counts the number of lines in a standard input.
Input: A string from the system's standard input
Output: A string wutg a total number if lines"""

import sys

count = 0
for line in sys.stdin: # standard input of the system
    count +=1

print(count,"lines in a standard input")

