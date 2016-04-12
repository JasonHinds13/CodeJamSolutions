#f = open("B-small-practice.in","r")
#o = open("small-output.out","w")

f = open("B-large-practice.in","r")
o = open("large-output.out","w")

n = int(f.readline())

ans = []

def rem(lis):
    for x in lis:
        if "\n" in x:
            lis[lis.index(x)] = x.strip()

def tostring(lis):
    if len(lis) > 1:
        s = ""
        for m in lis:
            if len(s) > 1:
                s = s+" "+m
            else:
                s += m
        return s
    else:
        for m in lis:
            return m

for i in range(0, n):
    x = str(f.readline()).split(" ")
    rem(x)
    x = tostring(x[::-1])
    ans.append("Case #"+str(i+1)+": " + x)

for a in ans:
    o.write(a+'\n')
    #print a
    
f.close()
o.close()

#answer for reverse
    
