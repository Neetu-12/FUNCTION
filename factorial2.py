# def factorial():
#     n=int(input("enter the no."))
#     i=1
#     f=1
#     while i<=n:
#         f=f*i
#         i=i+1
#     print(f)
# factorial()

a=["Delhi", "Delhi", "Mumbai", "Mumbai", "Delhi", "Chennai", 'Chennai']
i=0
r=[]
c=0
while i<len(a):
    if a[i] not in r:
        c=c+1
        r.append(a[i])
    i=i+1
print(r)