# kharcha=int(input("enter a no."))
# if kharcha<=50000:
#     print("hum budget k ander h")
# else kharcha>50000:
#     print("hum budget k ander h")
# else:
#     print("not")\
# def students():
#     n=int(input("enter a no."))
#     m=50000
#     if n<=m:
#         print("in budget")
#     else:
#         print("out of th budget")
# students()
def sum():
    n1=int(input("enter cost of food"))
    n2=int(input("total cost of laptop"))
    n3=int(input("cost of electricity bill"))
    n4=int(input("cost of playing things"))
    s=n1+n2+n3+n4
    if n1+n2+n3+n4<=50000:
        print("in budget")
    else:
        print("out of budget")
sum()