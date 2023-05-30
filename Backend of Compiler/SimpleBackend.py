n=int(input("Enter the Number of lines: "))
lines=[input("Line "+str(i+1)+":") for i in range(n)]
rCount=0
operator={'+':"ADD",'-':"SUB",'*':"MUL",'/':"DIV"}
for line in lines:
    result=line[0]
    opr1=line[2]
    opr2=line[4]
    print("MOV",opr1,"R"+str(rCount))
    print(operator[line[3]],opr2,"R"+str(rCount))
    print("MOV","R"+str(rCount),result)
    rCount+=1