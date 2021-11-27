# def add():
#     l1=[50, 60, 10] 
#     l2=[10, 20, 13]
#     print(l1[0]+l2[0],end=" ")
#     print(l1[1]+l2[1],end=" ")
#     print(l1[2]+l2[2],end=" ")
# add()

# l1=[50, 60, 10] 
# l2=[10, 20, 13] 
# i=0 
# r=[]
# while i<len(l1):
#     r.append(l1[i]+l2[i])
#     i=i+1
# print(r)

# n=int(input('enter no'))
# n1=int(input('enter no.'))
# i=2
# while i<=n1:
#     j=1
#     c=0
#     while j<=i:
#         if i%j==0:
#             c=c+1
#         j=j+1
#     if c==2:
    #     print(i)
    # i=i+1

# n=int(input("enter no."))
# i=2
# while i<=n:
#     j=1
#     c=0
#     while j<=i:
#         if i%j==0:
#             c=c+1
#         j=j+1
#     if c==2:
#         print(i)
#     i=i+1

def check_numbers_list(a,b):
    i=0
    while i<len(a):
        if a[i]%2==0 and b[i]%2==0:
            print('even h')
        else:
            print('even no. ni  h')
        i=i+1
check_numbers_list( [2, 6, 18, 10, 3, 75],[6, 19, 24, 12, 3, 87])