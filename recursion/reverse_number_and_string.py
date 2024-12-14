def reverseNumber(number: int) -> int:
    if number < 0:
        return -reverseNumber(-number)

    if number == 0:
        return 0

    return number % 10 * (10 ** len(str(number)) // 10) + reverseNumber(number // 10)


# print(reverseNumber(-1234))

def reverseString(text: str) -> str:
    if len(text) <= 1:
        return text

    return reverseString(text[1:]) + text[0]


print(reverseString("codelabpraveen"))
