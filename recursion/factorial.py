
def factorial(number):
    if number <1:
        return

    if number == 1:
        return 1

    return  number * factorial(number-1)


print(factorial(-1))

# -----------------------------------------------------------------------------------------------------

def factorial(number: int) -> int:
    """Calculating Factorial of number using recursion"""
    if number < 0:
        raise ValueError("Number is non-negative.")

    if number == 1:
        return 1

    return number * factorial(number - 1)


try:
    print(factorial(-1))
except ValueError as e:
    print(e)
