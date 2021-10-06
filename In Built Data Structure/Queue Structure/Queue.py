# Queue is a data structure which follows a specific order "FIFO" which stands for First in first out. 
# One that comes first gets served first and altered(such as deletion) too.
# Queue is mutable type structure. 

Q=[]
ch='y'
while ch=='y':
    print("1.Input")
    print("2.Delete")
    print("3.Display")
    choice=int(input("Enter your choice:"))
    if choice==1:
        a=input("Enter Values to be inserted:")
        Q.append(a)
    elif choice==2:
        if Q==[]:
            print("Empty queue")
        else:
            print("Deleted element is:",Q.pop(0))
    elif choice==3:
        l=len(Q)
        for i in range(0,l):
            print(Q[i])
    ch=input("Enter y to continue")        
