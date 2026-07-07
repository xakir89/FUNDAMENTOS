print()
for j in range (10):       
    for i in range(10):
        print("*", end=" ")     
    print()
print()

for i in range (10):
    j = 0
    while j <= i:
        
        print("*",end=" ")
        j+=1
    print()
print()

for i in range (1,6):
    
    for j in range(1,6):
        if i==1 and j==5:
            print(" "*(i+3),"*"*(i),end=" ")
        elif i ==2 and j == 4:
            print(" "*(i+1),"*"*(i+1),end=" ")
        elif i == 3 and j == 3:
            print(" "*(i-1),"*"*(i+2),end=" ")
        elif i == 4 and j == 2:
            print(" "*(i-3),"*"*(i+3),end=" ")
        elif i == 5 and j == 1:
            print(" "*(i-5),"*"*(i+4),end=" ")            
        else:
            continue
    print()
