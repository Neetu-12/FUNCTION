#######  main function

def add(a,b):
    c=a+b
    return c
def sub(x,y):
    z=x-y
    return z
def mult(k,f):
    d=k*f
    return d
def div(m,n):
    g=m//n
    return g
def main():
    if optn=="+":
        print(add(num1,num2))
    elif optn=="-":
        print(sub(num1,num2))
    elif optn=="*":
        print(mult(num1,num2))
    elif optn=="//":
         print(div(num1,num2))
    else:
        print("nothing")
num1=int(input("enter num1"))
num2=int(input("enter num2"))
optn=input("enter operation")
main()


# #### main function


def add(a,b):
    c=a+b
    return c
def sub(x,y):
    z=x-y
    return z
def mult(k,f):
    d=k*f
    return d
def main():
    print(add(4,4))
    print(sub(8,4))
    print(mult(2,3))
main()