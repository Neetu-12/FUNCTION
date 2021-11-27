# n=int(input("enter a no."))
# i=70
# c=0
# # while i<=1:
#     if n<70:
#         print("ok")
#     elif n>70:
#         c=c+1+5
#         print(c)
#     elif c>1:
#         print("licences suspended")
#     else:
#         pass
    # i=i+1
# n=int(input("enter a no."))    
# speed=70
# c=0
# c1=0
# if n<70:
#     c1=c1+1
#     print("speed ok")
# elif n>70:
#     speed=speed+5
#     c=c+c1+1
#     print(c)
# elif c>12:
#     print("licences suspended")
# else:
#     pass


def license(speed):
    points=(speed-70)//5
    if speed<70:
        print('ok')
    elif speed>=70 and speed<130:
        print(points,'warning! please do speed slow')
    else:
        print(points,'license suspended')    
license(speed=int(input('enter your speed')))