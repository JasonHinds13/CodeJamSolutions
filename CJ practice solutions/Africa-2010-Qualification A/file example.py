#f = open("A-small-practice.in","r")
#o = open("small-output.out","w")

f = open("A-large-practice.in","r")
o = open("large-output.out","w")

n = int(f.readline())

ans = []

for num in range(0,n):
    c = int(f.readline())
    i = int(f.readline())
    l = str(f.readline()).split(" ")
    
    l = [int(x) for x in l]
        
    for x in range(0, len(l)):
        for y in range(0, len(l)-1):
            if l[x]+l[y] == c and x != y and y < x:
                ans.append("Case #"+str(num+1)+": "+str(y+1)+" "+str(x+1))

for a in ans:
    o.write(a+"\n")
    print a

f.close()
o.close()
#Answer for store credit problem

