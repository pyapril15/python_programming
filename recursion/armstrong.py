def is_armstrong(number: int, num_digit=None) -> int:
    if number == 0:
        return 0

    if num_digit is None:
        num_digit = len(str(number))

    last_digit = number % 10

    return last_digit ** num_digit + is_armstrong(number // 10, num_digit)


def check_armstrong(number: int) -> bool:
    return number == is_armstrong(number)


num = 151

if check_armstrong(num):
    print(f"This is Armstrong number: {num}")
else:
    print(f"This is not Armstrong number: {num}")
