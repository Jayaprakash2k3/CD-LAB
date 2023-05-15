import re
Rules = {
    "INT#INT": "INT",
    "FLOAT#FLOAT": "FLOAT",
    "CHAR#INT": "INT",
    "INT#FLOAT": "FLOAT"
}
expr = input("Enter the Expression:")
expr = re.split("[-+*/=]", expr)
dtype = []
for each in expr:
    dtype.append(input("Enter the Data Type for "+each+":"))
current = dtype[1]
for i in range(2, len(dtype)):
    rFormat = current+"#"+dtype[i]
    if ((rFormat) in Rules):
        current = Rules[rFormat]
    else:
        print(expr[i]+" has to be converted to "+current)
        break
if (current == dtype[0]):
    print("Valid Type")
else:
    print("Final value must be "+dtype[0]+" but recived "+current)
