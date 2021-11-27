def harshad(num):
    sum=0
    n=num
    while num>0:
        rem=num%10
        sum=sum+rem
        num=num//10
    if n%sum==0:
        print('harshad number')
    else:
        print('not harshad number')
num=int(input('enter your number'))
harshad(num)