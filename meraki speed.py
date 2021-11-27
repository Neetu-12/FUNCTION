def license(speed):
    points=(speed-70)//5
    if speed<70:
        print('ok')
    elif speed>=70 and speed<130:
        print(points,'warning! please do speed slow')
    else:
        print(points,'license suspended')    
license(speed=int(input('enter your speed')))