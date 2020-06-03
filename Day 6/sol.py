from __future__ import print_function
n = int(input())
for i in range(n):
    s = input()
    s1 = list(s)
    l = len(s1)
    odd = ''
    even = ''
    for i in range(0,l):
        if i%2 == 0:
            even += str(s1[i])
        else:
            odd += str(s1[i])
    
    print (even, odd)
