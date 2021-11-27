def max(num1,num2,num3):
    if num1>num2 and num1>num3:
        if num2>num3:
            print(num1,'is max',num2,'is middle',num3,'is lowest')
        else:
            print(num1,'is max',num3,'is middle',num2,'is lowest')
    elif num2>num1 and num2>num3:
        if num1>num3:
            print(num2,'is gretest',num1,'is middle',num3,'is lowest')
        else:
            print(num2,'is gretest',num3,'is middle',num1,'is lowest')
    elif num3>num2 and num3>num1:
        if num2>num1:
            print(num3,'is gretest',num2,'is middle',num1,'is lowest')
        else:
            print(num3,'is gretest',num1,'is middle',num3,'is lowest')
    else:
        print('something went wrong! please recheck')
num1=int(input('enter your number'))
num2=int(input('enter your number'))
num3=int(input('enter your number'))

max(num1,num2,num3)



