n1=input("enter a char")
n2=input("enter a char")
i=0
while i<len(n1):
    if n1[i]>n2[i]:
        print(n1, "greater")
    elif n1[i]<n2[i]:
        print(n2,"lesser")
    elif n1[i]==n2[i]:
        print(n1,n2)
    else:
        print("not")
    i=i+1