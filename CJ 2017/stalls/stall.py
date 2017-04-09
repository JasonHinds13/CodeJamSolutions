f = open("C-small-1-attempt1.in", "r")
o = open("C-small-1-output1.out","w")

import math,sys

def build(n):
    z = []
    for i in range(n+2):
        if i == 0 or i == n+1:
            z.append(0)
        else:
            z.append(1)
    return z

def left(lis,s):
    c = 0
    s = s-1
    if lis[s] == 0:
        return c

    while s > 0:
        if lis[s] == 0:
            break
        s -= 1
        c += 1
    return c

def right(lis,s):
    c = 0
    for i in range(s, len(lis)):
        if lis[i+1] == 0:
            break
        c += 1
    return c

t = int(f.readline())

def half(lis,n,m,q):
    while n > 0:
        mid = int(math.ceil((m+q)/2.0))
        lis[mid] = 0
        q = mid
        n = n - 1
    return (lis,mid)

for i in range(t):
    s,p = f.readline().split(" ")
    s,p = int(s),int(p)

    ma,mi = 0,0

    if s == p:
        o.write("Case #"+str(i+1)+": "+ str(ma) + " "+ str(mi)+"\n")
        print "Case #"+str(i+1)+": "+ str(ma) + " "+ str(mi)

    else:
        lis = build(s)
        lis = half(lis,p,s,0)

        l = left(lis[0],lis[1])
        r = right(lis[0],lis[1])

        ma = max([l,r])
        mi = min([l,r])

        o.write("Case #"+str(i+1)+": "+ str(ma) + " "+ str(mi)+"\n")
        print "Case #"+str(i+1)+": "+ str(ma) + " "+ str(mi)

f.close()
o.close()