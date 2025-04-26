def factorial_recursion(i):
    if i == 0:
        return 1
    else:
        return i * factorial_recursion(i - 1)

print(factorial_recursion(5))