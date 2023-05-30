n=int(input("Enter number of Lines:"))
Icode = [input("Line "+str(i+1)+":").split("=") for i in range(n)]
left =  [Icode[i][0] for i in range(len(Icode))]
right = [Icode[i][1] for i in range(len(Icode))]
def print_code(info):
    print(info)
    print("------------------------")
    for i in range(len(left)):
        print(left[i],"=",right[i])
    print("------------------------")
print_code("Original")

for i in range(len(Icode)):
    try:
        right[i]=str(eval(right[i]))
    except:
        pass
print_code("Constant Folding")

for i in range(len(Icode)-2):
    if left[i] not in "".join(right[i:]):
        left.pop(i)
        right.pop(i)
print_code("Dead Code Elimination")

for i in range(len(right)-2):
    if(right[i] in right[i+1:]):
        index=right[i+1:].index(right[i])+i+1
        lftVal=left.pop(index)
        right.pop(index)
        right=[a.replace(lftVal,left[i]) for a in right]
    
print_code("Common Expression Elimination")