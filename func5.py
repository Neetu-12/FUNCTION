# def first_function():
#     s = 'I love India'
#     def second_function():
#         s = "MY NAME IS JACK"
#         print(s)     
#     second_function()
#     print(s)    
 
# first_function()

# def add():
#     age=int(input("enter your age"))
#     if age<18:
#         print("you are not eligible for vote ")
#     elif age>=18:
#    (     print("you are eligible for vote ")
#     else:
#         print("nothing")
# add()

# guess=7
# i=1
# while i<=3:
#     n=int(input("enter no."))
#     if n==guess:
#         print("you r right")
#     elif n<guess:
#         print("your guess is wrong because it's less")
#     elif n>gess:
#         print("greater than guessing no.")
#     # elif n==10:
#     #     break
#     else:
#         if n==10:
#             break
#         else:
#             print("upps you out of the game")
#     i=i+1
# n=int(input("enter the no."))
# l=['A','B']
# i=0
# while i<len(l):
#     n=int(input("enter the no."))

# from abc import abstractmethod


# def add():
#     n=int(input("enter the no."))
#     i=1
#     s=0
#     while i<n:
#         a=n%i
#         if a==0:
#             s=s+i
#         i=i+1
#     if n==s:
#         print("perfect")
#     else:
#         print("not perfect")
# add() 

j=1
while j<=100:
    n=j
    i=1
    sum=0
    while i<n:
        if n%i==0:
            sum+=i
        i+=1
    if sum==n:
        print("perfect number",n)
    j+=1
