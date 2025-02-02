import math


def sumF(number1,number2):
    return number1+number2

def diffF(number1, number2):
    return number1-number2

def sq(num1):
    return num1*num1

def sq_eq(a,b,c):
    D=sq(b)-(4*a*c)
    if D>0:
        x1=(-b+math.sqrt(D))/(2*a)
        x2=(-b-math.sqrt(D))/(2*a)
        return x1,x2
    else:
        x=-b/(2*a)  
        return x

def avg(numbersList):
    res=sum(numbersList)/len(numbersList)
    return res

def mediana(numbers):
    numbers.sort()
    if len(numbers)%2==1:
        pos=int((len(numbers)+1)/2)
        return numbers[pos-1]
    else:
        pos=int(len(numbers)/2)
        pos2=pos+1
        return (numbers[pos-1]+numbers[pos2-1])/2

def moda(numbers):
    numDict={}
    for i in range(len(numbers)):
        currentNum=numbers[i]
        if currentNum in numDict:
            numDict[currentNum]+=1
        else:
            numDict[currentNum]=1
    maxV=max(numDict.values())
    maxV_list=[]
    for k,v in numDict.items():
        if v==maxV:
            maxV_list.append(k)
    #[k for (k,v) in numDict.items() if v==maxV]
    return maxV_list
