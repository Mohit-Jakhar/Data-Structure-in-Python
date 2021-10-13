# Adding deleting and modifying data stored in a stack.

stack=eval(input("Enter stack:"))
ch="y"
while ch=="y":
    print("1.PUSH")
    print("2.POP")
    print("3.DISPLAY")
    choice=int(input("Enter your choice:"))
    if choice==1:
        A=input("Enter any number:")
        stack.append(A)
    elif choice==3:
        l=len(stack)
        for i in range(l-1,-1,-1):
         print(stack[i])
    elif choice==2:
        if stack==[]:
            print("Empty stack")
        else:    
            print("Deleted element:",stack.pop())

    ch=input("Enter y to continue or not")   
