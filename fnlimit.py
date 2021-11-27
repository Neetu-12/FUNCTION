# def show_numbers(even,odd,even1,odd1):
#     print(even+odd+even+odd)
# show_numbers(even=0,odd=1,even1=2,odd1=3)

def show_function(limit):
    n=int(input("enter a no."))
    i=0
    while i<=n:
        if i%2==0:
            print("enen ",i)
        if i%2!=0:
            print("odd",i)
        i=i+1
show_function(0)

