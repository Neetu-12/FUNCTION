def sum():
    i=1
    s=0
    while i<=3:
        n=int(input("enter a no."))
        s=s+n
        i=i+1
    avg=s//3
    print(avg,s)
sum()