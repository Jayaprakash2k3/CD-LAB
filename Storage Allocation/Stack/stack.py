stack =[]
def push(val):
  return stack.append(val)
def pop():
    if(len(stack)):
        return stack.pop()
    else:
        return  -1
def peek():
    if(len(stack)):
        return stack[-1]    
    else:
        return -1
def show():
    for each in stack:
        print(each)
choice=0
while(choice!=5):
    choice=int(input("1.PUSH 2.POP 3.PEEK 4.SHOW 5.EXIT\nEnter your choice: "))
    if(choice==1):
        print("Enter the value to be pushed")
        push(int(input()))
        print("Pushed:",peek(),"\n")
    elif(choice==2):
        print("Popped:",pop(),"\n")
    elif(choice==3):
        print("Peek:",peek(),"\n")
    elif(choice==4):
        show()
