def gcd(a: int, b: int) -> int:
    if b == 0:
        return a

    return gcd(b, a % b)


num1 = 32
num2 = 28

result = gcd(num1, num2)

print(f"The gcd of {num1} and {num2} is {result}")
