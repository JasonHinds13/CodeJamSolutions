n = int(raw_input())

ans = []

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
    x = str(raw_input()).split(" ")
    x = tostring(x[::-1])
    ans.append("Case #"+str(i+1)+": " + x)

for a in ans:
    print a

#answer for reverse
    
