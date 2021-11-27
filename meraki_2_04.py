def showNumbers(limit):
    i=0
    while i<=limit:
        if i%2==0:
            print(i,"even")
        else:
            print(i,'odd')
        i=i+1
limit=int(input('enter your limit'))
showNumbers(limit) 