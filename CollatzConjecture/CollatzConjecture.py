chainlist = []
maxchain=[]

for i in range(3,1001):
    chainlist.clear()
    chainlist.append(i)
    while i>1: 
        #If Number is even, #/2
        if(i%2==0):
            i = int(i / 2)
        #If Number is odd, 3*# + 1
        elif(i%2!=0):
            i = int(3 * i) + 1      
        chainlist.append(i)
    #Only change largest chain when a new one is found
    if(len(chainlist)>len(maxchain)):
        maxchain.clear()      
        maxchain = list(chainlist)

print(f"Number with Longest Chain: {maxchain[0]}")
print(f"Chain:{maxchain}")
print(f"Chain Length: {len(maxchain)}")
