# Enter your code here. Read input from STDIN. Print output to STDOUT
import time
from math import radians, cos, sin, asin, sqrt

def conv_time(t):
    return int((t.split(" ")[1]).replace(":",""))

def conv_date(d):
    date = d.split(" ")[0]
    return time.strptime(date, "%m/%d/%Y")

def get_nums(lis):
    l = []
    for d in lis:
        l.append(d["PhoneNumber"])
    return l

def getbynum(lis, num):
    for x in lis:
        if x["PhoneNumber"] == num:
            return x

inp = raw_input().split(",")

lat1 = radians(float(inp[0]))
long1 = radians(float(inp[1]))

r = 6378.137
rk = float(raw_input()) #radius she wants to reach

direc = {}
c = 0 #counter

res = [] #will store only number
getall = [] #will store all info relating

header = raw_input().split(",")

while(True):
    
    try:
        n = raw_input().split(",")
    
        direc[c] = {header[0]: n[0], header[1]: n[1], header[2]: n[2], header[3]: n[3]}
    
        lat2 = radians(float(direc[c]["Latitude"]))
        long2 = radians(float(direc[c]["Longitude"]))
    
        d = 2 * r * asin(sqrt (sin((lat2 - lat1)/2)**2 + cos(lat1) * cos(lat2) * sin((long2 - long1)/2)**2))
    
        if d < rk and direc[c]["PhoneNumber"] not in res: 
            res.append(direc[c]["PhoneNumber"])
            getall.append(direc[c])
            
        elif d >= rk and direc[c]["PhoneNumber"] in get_nums(getall):
            x = direc[c]["PhoneNumber"]
            y = getbynum(getall, x)
            
            #current one
            td = conv_date(direc[c]["Date&Time"])
            tc = conv_time(direc[c]["Date&Time"])
            
            #one in list
            ld = conv_date(y["Date&Time"])
            lc = conv_time(y["Date&Time"])
            
            if (tc > lc and td >= ld) or (td > ld):
                res = [m for m in res if m != x]

        c+=1
        
    except EOFError:
        break
    
res.sort()    
print ",".join(res)
