def string(num1,num2):
    if num1=="":
        num1=0
    elif num2=="":
        num2=0

    a=int(num1)
    b=int(num2)
    c=a+b
    d=str(c)
    print(d)



num1=input('enter your number')
num2=input('enter your number')
string(num1,num2)

