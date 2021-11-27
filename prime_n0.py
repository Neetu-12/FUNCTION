def prime_number(num):
    i=1
    c=0
    while i<=num:
        if num%i==0:
            c=c+1
        i=i+1
    if c==2:
        print(num,'prime no.')
    else:
        print(num,'not prime number')
num=int(input('enter your number'))
prime_number(num)