def cal(a,b):
    add=a+b
    sub=a-b
    mul=a*b
    return (add,sub,mul)
n=int(input('enter your number'))
m=int(input('enter your number'))
print(cal(n,m))