def perfect(num):
    i=1
    sum=0
    while i<num:
        if num%i==0:
            sum=sum+i
        i=i=1
    if sum==num:
        print("perfect number")
    else:
        print('not perfect number')
perfect(num=int(input('enter a number')))

def perfect():
    i=1
    while i<=1000:
        j=1
        sum=0
        while j<i:
            if i%j==0:
                sum=sum+j
            j=j+1
        if sum==i:
            print(sum,'is perfect number')
        else:
            pass
        i=i+1
perfect()
