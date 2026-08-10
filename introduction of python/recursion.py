# 3998979
def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:

        return num * factorial(num -1)

print(factorial(5))
print(factorial(0))
print(factorial(9))
