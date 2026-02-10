from typing import List

source = [9,8,7,6,5,4,3,2,1]
aux = []
dest = []

def hanoi(n, source, aux, dest):
    if n == 1:
        dest.append(source.pop())
    else:
        hanoi(n-1, source, dest, aux)
        dest.append(source.pop())
        hanoi(n-1, aux, source, dest)
    
##hanoi(9, source, aux, dest)
##print(source, aux, dest)

def validBraces(n: int) -> List [str]:
    valids = []
    if n == 0:
        return [""]
    elif n == 1:
        return ["()"]
    else:
        for j in range(1, (n+1)//2+1):
            valids += [a + b for a in validBraces(j) for b in validBraces(n-j)]
            valids += [b + a for a in validBraces(j) for b in validBraces(n-j)]

        valids += ["(" + a + ")" for a in validBraces(n-1)]
        return list((valids))
    
print(len(validBraces(7)))
        
    