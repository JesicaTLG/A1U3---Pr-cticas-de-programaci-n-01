


def paren(symbolString):
    
    s = []
    index = 0
    balanced = True
    
    while index<len(symbolString) and balanced:
        symbol = symbolString[index]
        if(symbol in '({['):
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol):
                     balanced = False
        index = index + 1
    if s.isEmpty() and balanced:
        return True
    else:
        return False
    
def matches(open,close):
    if '({['.index(open) == ')}]'.index(close):
        return True
    else:
        return False

print(paren("((([])))"))


