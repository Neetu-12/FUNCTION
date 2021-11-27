# a=[{'id': 1, 'success': True, 'name': 'Lary'},
#  {'id': 2, 'success': False, 'name': 'Rabi'},
#  {'id': 3, 'success': True, 'name': 'Alex'}]
# c=0
# r=[]
# for i in a:
#     for j in a[i]:
#         if a[i]
#         c=c+1
#         r.append(c)
#     print(r)

a=[1, 2, 3, 4]
b=["neetu","baby","suraj","neha"]
i=0
r=0
s=""
while i<len(a):
    j=0
    while j<len(a):
        s=s+a[i]
        r.update({s:j})
        j=j+1
    i=i+1
print(r)
