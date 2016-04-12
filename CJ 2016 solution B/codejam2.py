f = open("B-small-attempt0.in","r")
#f = open("test.txt","r")
o = open("small-output.out","w")

'''
To solve this problem we look for a combination of '+-' in the string
If we find one we flip the elements from the first element to the plus we found
we do this until we can't get '+-' anymore.
we then look for the combination '-+' and from there flip all elements from
the first to the '-' inclusive and we should arrive at a full happy stack.
'''

ans = []

def flip(lis):
    if lis == ['-','+']:
        return ['+','+']
    
    elif lis == ['+','-']:
        return ['-','-']
    
    elif lis == ['-']:
        return ['+']
    
    elif lis == ['+']:
        return ['-']
    
    else:
        counter = 0
        lis = lis[::-1]
        for x in lis:
            if x == '+':
                lis[counter] = '-'
            else:
                lis[counter] = '+'
            counter += 1
        return lis

T = int(f.readline())

for i in range(T):

    count = 0

    S = str(f.readline())
    #if i == 72: print S ###case 73 was not working
    
    S = [x for x in S]

    while True:
        if '-' not in ''.join(S):
            break
        elif '+' not in ''.join(S):
            count += 1
            break

        elif '+-' in ''.join(S):
            for x in range(0, len(S)):
                for y in range(0, len(S)):
                    if S[x]+S[y] == '+-' and y-x == 1:
                        #print ''.join(S) + " *****Original" ###
                        S[0:y+1] = flip(S[0:y+1])
                        if i == 72: print ''.join(S) ####
            count += 1
        
        elif ('-+' in ''.join(S))  or ('+' not in ''.join(S)):
            for x in range(0, len(S)):
                for y in range(0, len(S)):
                    if S[x]+S[y] == '-+' and y-x == 1:
                        #print ''.join(S) + " **ORIGIN" ###
                        #print S[0:y] ###
                        S[0:y] = flip(S[0:y])
                        if i == 72: print ''.join(S) ###1111

            count += 1
    #ans.append("Case #"+str(i+1)+": "+str(count))
    o.write("Case #"+str(i+1)+": "+str(count)+"\n")
    print "Case #"+str(i+1)+": "+str(count)

#for a in ans:
    #o.write(a+"\n")
    #print a

f.close()
o.close()
