# Enter your code here. Read input from STDIN. Print output to STDOUT
Q = int(raw_input())

def gcd(x,y):
    while x*y != 0:
        if x >= y: 
            x = x % y
        else: 
            y = y % x
    return x+y

for i in range(Q):
    s = raw_input().split(" ")
    
    n = int(s[0])
    a = int(s[1])
    b = int(s[2])
    
    sums = sum([x for x in range(a,b+1) if gcd(n,x) == 1])

    print sums % 1000000007
