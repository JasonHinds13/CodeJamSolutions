# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(raw_input())

def getmin(lis):
    mini = 10**5
    x = 0
    y = 0
    for m in lis:
        for n in lis:
            if abs(m - n) > 0 and abs(m-n) < mini:
                mini = abs(m-n)
                x = m
                y = n
    return [mini, x, y]

def getmin2(lis, n):
    sums = 0
    for i in range(n):
        x = getmin(lis)
        sums += x[0]
        lis = [m for m in lis if m != x[1] or m != x[2]]
    return sums

for i in range(T):
    inp = raw_input().split(" ")

    n = int(inp[0])
    k = int(inp[1])

    pwrs = []

    for x in range(n):
        pwrs.append(int(raw_input()))
        
    if n%k == 0:
        print getmin(pwrs)[0]
    else:
        print getmin2(pwrs, n%k)
