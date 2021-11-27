def positive_nagative(list1):
    i=0
    c1=0
    c2=0
    while i<len(list1):
        if list1[i]>0:
            c1=c1+1
        else:
            c2=c2+1
        i=i+1
    print(c1,'positive number')
    print(c2,'negative numbers')  
positive_nagative(list1 = [2, -7, 5, -64, -14])  
            