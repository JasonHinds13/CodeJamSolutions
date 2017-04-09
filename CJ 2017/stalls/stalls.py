#f = open("C-small-1-attempt0.in", "r")
#o = open("C-small-1-output.out","w")
f = open("test.in","r")
o = open("output.out","w")

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

def getIdeal(lis):
    new = []
    k = []
    l = []
    ma,mi = 0,0

    for m in lis:
        new.append(min(m))

    for m in lis:
        if max(new) in m:
            k.append(m)

    ma = max(new)

    new = []
    for m in k:
        new.append(max(m))

    mi = max(new)

    for m in lis:
        if ma in m and mi in m:
            l.append(m)
        elif max(new) in m:
            l.append(m)

    return l[0],mi,ma

t = int(f.readline())

for i in range(t):
    s,p = f.readline().split(" ")
    s,p = int(s),int(p)

    ma,mi = 0,0

    if s == p:
        o.write("Case #"+str(i+1)+": "+ str(ma) + " "+ str(mi)+"\n")
        print "Case #"+str(i+1)+": "+ str(ma) + " "+ str(mi)

    else:
        lis = build(s)

        for x in range(p):
            new = []
            #mins = []
            #maxs = []
            for n in range(1,s+1):
                if lis[n] != 0:
                    lis[n] = (left(lis,n),right(lis,n))
                    #mins.append(min(lis[n]))
                    #maxs.append(max(lis[n]))
                    new.append(lis[n])
            #ma = max(mins)
            #mi = max(maxs)
            r = getIdeal(new)
            q = r[0]
            ma,mi = r[1],r[2]
            e = lis.index(q)
            lis[e] = 0

        o.write("Case #"+str(i+1)+": "+ str(ma) + " "+ str(mi)+"\n")
        print "Case #"+str(i+1)+": "+ str(ma) + " "+ str(mi)

f.close()
o.close()