class node:
    def __init__(self,data,left,right):
        self.operation=data
        self.Left=left
        self.Right=right
n=int(input("Enter the number of 3 Address Code:"))
data=[input("Enter the code for "+str(i+1)+":") for i in range(n)]
leaf=node(["null"],None,None)
nodeList={}
for each in data:
    result = each[0]
    opr1 = each[2]
    opr2 = each[4]
    if(opr1 not in nodeList):
        nodeList[opr1] = node([opr1], leaf, leaf)
    if(opr2 not in nodeList):
        nodeList[opr2] = node([opr2], leaf, leaf)
    operator = node([each[3],result], leaf, leaf)
    operator.Left=nodeList[opr1]
    operator.Right=nodeList[opr2]
    nodeList[result]=operator
for each in nodeList:
    print("["+",".join(nodeList[each].Left.operation)+"]",end="")
    print("<<["+",".join(nodeList[each].operation)+"]>>",end="")
    print("["+",".join(nodeList[each].Right.operation)+"]")

    