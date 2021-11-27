def factorial(num):
     i=1
     c=1
     while i<=num:
        c=c*i
        i=i+1
        print(c)
num=int(input('enter your number'))
factorial(num)