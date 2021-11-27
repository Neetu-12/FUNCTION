# def num(list):
#     i=0
#     max=0
#     while i<len(list):
#         if list[i]>max:
#             max=list[i]
#         i=i+1
#     min=max
#     j=0
#     while j<len(list):
#         if list[j]<min:
#             min=list[j]
#         j=j+1
#     print(min)
# num(    list = [8, 6, 4, 8, 4, 50, 2, 7])                             

def add():
    list = [8, 6, 4, 1, 4, -50, 2, 7]
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
add()