# l1 = [1, 342, 75, 23, 98]
# l2 = [75, 23, 98, 12, 78, 10, 1]
# r=[]
# i=0
# while i<len(l1):
#     j=0
#     while j<len(l2):
#         if l1[i]==l2[j]:
#             r.append(l1[i])
#         j=j+1
#     i=i+1
# print(r)

l1 = [1, 5, 10, 12, 16, 20]
l2 = [1, 2, 10, 13, 16]
r=[]
r2=[]
i=0
while i<len(l1):
    j=0
    s=[]
    while j<len(l2):
        if l1[i]==l2[j]:
            s.append(l1[i])
        r.extend(l1[i])
        r2.extend(r)
        j=j+1
    i=i+1
print(r2)
