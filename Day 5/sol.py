import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    for i in range(1, 11):
        a = str(n) + ' x ' + str(i) + ' = ' + str(n*i)
        sys.stdout.write (a + '\n')
