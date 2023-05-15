NFA={'S':{0:{"A"},1:{"S","B"}},
     'A':{0:{"A","B"},1:{"S"}},
     'B':{0:{"A"},1:{"S","A"}}}
DFA={}
States=['S']
while States:
    Current = States.pop(0)
    try:
        for each in NFA[Current]:
            NFACurrent ="".join(sorted(NFA[Current][each]))
            if(NFACurrent not in DFA):
                States.append(NFACurrent)
            try:
                DFA[Current][each]=NFACurrent
            except:
                DFA[Current]={}
                DFA[Current][each]=NFACurrent
    except:
        zero=set()
        ones=set()
        for a in Current:
            zero=zero|NFA[a][0]
            ones=ones|NFA[a][1]
        zero ="".join(sorted(zero))
        ones ="".join(sorted(ones))
        DFA[Current]={0:zero,1:ones}
        if(zero not in DFA):
            States.append(zero)
        if(ones not in DFA):
            States.append(ones)
for each in DFA:
    print(each+" =>",DFA[each])