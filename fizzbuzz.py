# If the number is divisible by 3, it should return “Fizz”.
# If it is divisible by 5, it should return “Buzz”.
# If it is divisible by both 3 and 5, it should return “FizzBuzz”.
# Otherwise, it should return the same number.
def fizz_buzz(num):
    if num%3==0:
        return 'fizz'
    if num%5==0:
        return 'buzz'
    if num%5==0 and num%3==0:
        return 'fizz buzz'
    else:
        return num
a=fizz_buzz(num=int(input('enter your number')))
print(a)
        

