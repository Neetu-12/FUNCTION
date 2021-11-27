# def harshad(n): 
#     sum=0
#     while n>0:
#         a=n%10
#         sum=sum+a
#         n=n//10
#     if n%sum==0:
#         print("harshad no")
#     else:
#         ("not harshad")
# n=int(input("enter any no."))
# harshad(n)


# n=int(input("enter any no."))
# t=n
# sum=0
# while t>0:
#     a=t%10
#     sum=sum+a
#     t=t//10
# if t%sum==0:
#     print("harshad no")
# else:
#     ("not harshad")

# def harshad(num):
#     sum=0
#     n=num
#     while num>0:
#         rem=num%10
#         sum=sum+rem
#         num=num//10
#     if n%sum==0:
#         print('harshad number')
#     else:
#         print('not harshad number')
# num=int(input('enter your number'))
# harshad(num)


n=int(input("enter a no."))
s=0
while n>0:
    a=n%10
    s=s+a
    n=n//10
if n%s==0:
    print("harshad no.")
else:
    print("not harshad")