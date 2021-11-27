def num(numbers):
    i=0
    max=0
    while i<len(numbers):
        if numbers[i]>max:
            max=numbers[i]
        i=i+1
    print(max)
num(numbers = [3, 5, 7, 34, 2, 89, 2, 5])                    #max in  function..........


def num(numbers):
    i=0
    sum=0
    while i<len(numbers):
        sum=sum+numbers[i]
        i=i+1
    print(sum)
num(numbers = [1, 2, 3, 4, 5])                    #sum in function...................

def num(list):
    i=-1
    reverse_list=[]
    while i>-10:
        reverse_list.append(list[i])
        i=i-1
    print(reverse_list)
num(    list = ["Z", "A", "A", "B", "E", "M", "A", "R", "D"])                        # of lidt in function..........

def num(list):
    i=0
    max=0
    while i<len(list):
        if list[i]>max:
            max=list[i]
        i=i+1
    min=max
    j=0
    while j<len(list):
        if list[j]<min:
            min=list[j]
        j=j+1
    print(min)
num(    list = [8, 6, 4, 8, 4, 50, 2, 7])                              #minimum in a list in ction


