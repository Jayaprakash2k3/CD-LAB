import re
f=open("input.c")
code = f.readlines()
size ={"int":4,"float":4,"double":8,"char":1} # default size
code =[a.strip().replace("\n","") for a in code] # remove new line
symbol = {}
for line in code:
    if (re.search("^(int|float|double|char) .*",line)):
        # to check if its a declarative statement
        words = line.replace(" ","#").replace(",","#").replace(";","").split("#")
        for word in words[1:]:# because words[0] is dtype
            symbol[word]={
                "Type":words[0],
                "Size":size[words[0]],
                "Variable":word,
                "Address":id(word),
                "isFunction":"(" in word and ")" in word,
                "Line of Decleartion":code.index(line)+1,
                "Usage":[]
            }

for each in symbol:
    print(each,symbol[each])