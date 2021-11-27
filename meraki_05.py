def number(num1,num2):#:.............................que 05 part1
    if num1%2==0 and num2%2==0:
        print('even')
    else:
        print('odd')
number(24,23)
number(234,456)

def number(list1,list2):
    i=0
    while i<len(list1):
        if list1[i]%2==0 and list2[i]%2==0:
            print("both are even")
        else:
            print('both  are not even')
        i=i+1
number(list1=[2, 6, 18, 10, 3, 75],list2=[6, 19, 24, 12, 3, 87] )           #que 05 part2......................