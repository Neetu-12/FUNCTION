def max(list1):
    i=0
    a=0
    while i<len(list1):
        if list1[i]>a:
            a=list1[i]
        i=i+1
    print(a,'max in list')
max(list1=[4,6,2,1,9,63,-134,566]) 
def min(list1):
    i=0
    a=0
    while i<len(list1):
        if list1[i]<a:
            a=list1[i]
        i=i+1
    print(a,'min in list')
min(list1=[4,6,2,1,9,63,-134,566])