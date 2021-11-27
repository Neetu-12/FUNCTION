def even_odd(limit):
#     if limit%2==0:
#         print('even')
#     else:
#         print('odd')
# limits(limit=int(input('enetr your number')))
    i=0
    while i<limit:
        if i%2==0:
            print('even')
        else:
            print('odd')
        i=i+1
limit=int(input('enetr your number'))
even_odd(limit)