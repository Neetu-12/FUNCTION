def calculate(sign,num1,num2):
    if sign=="+":
        add=num1+num2
        return add
    elif sign=="-":
        sub=num1-num2
        return sub 
    elif sign=="*":
        mul=num1*num2
        return mul
    elif sign=="/":
        div=num1/num2
        return div
sign=input('enter your symbol')
num1=int(input('enter your number'))
num2=int(input('enter your number'))
print(calculate( sign,num1,num2))