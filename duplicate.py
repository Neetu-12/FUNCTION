# def duplicate(list1):
#     i=0
#     a=[]
#     while i<len(list1):
#         if list1[i] not in a:
#             a.append(list1[i])
#         else:
#             pass
#         i=i+1
#     print(a)
# duplicate(list1=[1,2,3,3,3,3,4,5])


# def duplicate(string_list):
#     i=0
#     string_list2=[]
#     while i<len(string_list):
#         if string_list[i] not in string_list2:
#             string_list2.append(string_list[i])
#         else:
#             pass
#         i=i+1
#     print(string_list2)
# duplicate(string_list= ["Rishabh", "Rishabh", "Abhishek", "Rishabh", "Divyashish", "Divyashish"])

# def duplicate(list1,list2):
#     i=0
#     list3=[]
#     while i<len(list1):
#         if list1[i] in list2:
#             list3.append(list1[i])
#         i=i+1
#     print(list3)
# list1 = [1, 342, 75, 23, 98]
# list2 = [75, 23, 98, 12, 78, 10, 1]
# duplicate(list1,list2)

# def duplicate(list1,list2):
#     i=0
#     list3=[]
#     while i<len(list1):
#         if list1[i] in list2 and list1[i] not in list3:
#             list3.append(list1[i])
#         i=i+1
#     print(list3)
# list1 = [1, 5, 10, 12, 16, 20]
# list2 = [1, 2, 10, 13, 16]
# duplicate(list1,list2)

def duplicate(list1,list2):
    i=0
    j=0
    list3=[]
    while i<len(list1) and j<len(list2):
        if list1[i] not in list3:
            list3.append(list1[i])
        i=i+1 
        if list2[j] not in list3:
            list3.append(list2[j])
        
        j=j+1
    print(list3)
list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16]
duplicate(list1,list2)