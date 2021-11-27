# def max():
#     a=[3, 5, 75, 28, 2, 5]
#     m=0
#     m1=0
#     i=0
#     while i<len(a):
#         if a[i]>m:
#             m1=m
#             m=a[i]
#         i=i+1
#     print("max",m)
#     print("sec max",m1)
# max()
# def add():
#     a = ["Z", "A", "A", "B", "E", "M", "A", "R", "D"]
#     i=-0
#     r=[]
#     while i>-len(a):
#         i=i-1
#         r.append(a[i])
#     print(r)
# add()

a=[8, 6, 4, 8, 4, 50, 2, 7]
i=0
min=0
max=0
while i<len(a):
    if a[i]<min:
        min=a[i]
    elif a[i]>max:
        max=a[i]
    i=i+1
print(max)
print(min)


















# # sum sum
# def sum():
#     n = [1, 2, 3, 4, 5]
#     s=0
#     i=0
#     while i<len(n):
#         s=s+n[i]
#         i=i+1
#     print(s)
# sum()


# a=[10,1,9,2,8,3,7,4,5,6]
# i=0
# while i<len(a):
# 	a.sort()
# 	i=i+1
# print(a)

# a=[6, 8, 4, 3, 9, 56, 0, 34, 7, 15]
# a.sort()
# print(a)
# def add():
#     a=[6, 8, 4, 3, 9, 56, 0, 34, 7, 15]
#     i=0
#     while i<len(a):
#         a.sort()
#         i=i+1
#     print(a)
# add()
# 


# reverse in function

# a=["Z", "A", "A", "B", "E", "M", "A", "R", "D"]
# i=-1
# s=""
# while i>-len(a):
#     b=a[i]


# n=input("enter no.")a=["Z", "A", "A", "B", "E", "M", "A", "R", "D"]
# i=-1
# s=""
# while i>-len(a):
#     b=a[i]

# n=input("enter name ")
# i=-1
# s=''
# while i>-len(n):
#     a=n[i]
#     s=s+a
#     i=i-1
# if n==s:
#     print("palindrom")