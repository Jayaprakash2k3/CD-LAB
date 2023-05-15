# This is equivalent to C++ Code
# We use simple List instead of LinkedList
# We do not use pointers in Python 
class Student:
    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks
    def address(self):
        return id(self)

    def __str__(self):
        return self.name+" "+str(self.roll)+" "+str(self.marks)+" "+str(id(self))

choice=0
Heap=[]
while(choice!=5):
    choice=int(input("1.PUSH 2.POP 3.PEEK 4.SHOW 5.EXIT\nEnter your choice: "))
    if(choice==1):
        Heap.append(Student(input("Name:"),input("Roll:"),input("Marks:")))
        print("Heap has been Created")
    elif(choice==2):
        print("Popped:",Heap.pop(),"\n")
    elif(choice==3):
        print("Peek:",Heap[-1],"\n")
    elif(choice==4):
        for each in Heap:
            print(each)


