# a=[["n","e"],["e","t","u"]]
# i=0
# r=[]
# while i<len(a):
#     r.extend(a[i])
#     i=i+1
# print(r)

# a=[["n","e"],["e","t","u"]]
# i=0
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         while j<len(a[i]):
#             j=j+1
#     i=i+1
#     print(a[i][j])
# list1=[ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
# i=0
# r=[]
# while i<len(list1):
#     if type(list1[i])==list:
#         j=0
#         s=[]
#         while j<len(list1[i]):
#             s.append(list1[i][j])
#             b=s+list1[i][j]
#             j=j+1
#         r.append(b)
#     i=i+1             
# print(r)
def my_function(*kids):
  print(*kids)
my_function("Emil", "Tobias", "Linus")

# Q=1:

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

Q=1

n=input("enter name")
i=0
while i<=1:
    n=input("enter name")
    if n>"A" and n<="Z":
        print("upper case")
    elif n>"a" and n<="z":
        print("lower case")
    else:
        print("nothing")
    i=i+1

# a= [6,1,3,5,8,9,9,9,6,3,1]
# i=0
# produact=1
# while i<len(a):
#     print(product*(a[i]))  
#     i=i+1     