from __future__ import print_function
n = int(input())

d = {}

for i in range(n):
    name, number = input().split()
    
    d[name]=number

while(True):
    try:
        name = input()
    except EOFError:
        break
    
    if name in d:
        print ("{}={}".format(name,d[name]))
    else:
        print("Not found")
