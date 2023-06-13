import math
L0 = int(input()) # for the first input
L1 = input() # for the second input
L2 = list(L1.split(" ")) #we split it into a list since it's eneterd in this form (1 2 3 4 5)
L3 = []
for i in L2:
    i = int(i)
    L3.append(i) # we make an int list out of it 
A = 0
z=1
while A<=len(L3)-1:
    z = (z* L3[A]) % (pow(10,9)+7) # we apply the required operations and store them 
    A+=1
print(z)    #we print!
    
