def add():
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
add()



# ##q=2

x=1
y=2
x, y, z = x, x, y
z, y, z = x, y, z
print(x,y,z)

