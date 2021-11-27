# def func(x = 1, y = 2):
#     x = x + y
#     y += 1
#     print(x, y)
# func(y = 2, x = 1)
num = 1
def func():
    global num
    num = num + 3
    print(num)

func()
print(num)
