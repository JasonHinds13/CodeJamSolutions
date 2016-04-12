f = open("A-small-practice.in","r")

n = int(raw_input())

ans = []

for num in range(0,n):
    c = int(raw_input())
    i = int(raw_input())
    l = raw_input().split(" ")
    
    l = [int(x) for x in l]
        
    for x in range(0, len(l)):
        for y in range(0, len(l)-1):
            if l[x]+l[y] == c and x != y and y < x:
                ans.append("Case #"+str(num+1)+": "+str(y+1)+" "+str(x+1))

for a in ans:
    print a

#Answer for store credit problem

