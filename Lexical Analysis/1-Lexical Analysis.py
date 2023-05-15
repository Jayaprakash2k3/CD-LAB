import re
def tokenize_cpp(code):
    keywords = ['int', 'char', 'double', 'float',
                'void', 'if', 'else', 'for', 'while', 'return']
    tokens = []
    code = code.strip()
    while code:
        if code[0].isdigit():
            match = re.match('^\d+', code)
            tokens.append(('NUMBER', match.group(0)))
            code = code[match.end(0):]
        elif code[0].isalpha() or code[0] == '_':
            match = re.match('^\w+', code)
            word = match.group(0)
            if word in keywords:
                tokens.append(('KEYWORD', word))
            else:
                tokens.append(('IDENTIFIER', word))
            code = code[match.end(0):]
        else:
            if (code[0] == ' '):
                pass
            else:
                tokens.append(('SYMBOL', code[0]))
            code = code[1:]
    return tokens
code = open("input.c").read().replace('\n', '')
tokens = tokenize_cpp(code)
for each in tokens:
    print(each)
