def sum(num1,num2,num3):
    if num1>num2:
        print("num2 is greater")
    elif num1>num3:
        print("num3 is greater")
    else:
        print("num1 is greater")
a=int(input("enter a no."))
b=int(input("enter a no."))
c=int(input("enter a no."))
sum(a,b,c)