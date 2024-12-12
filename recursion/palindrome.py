def is_palindrome(text: str, start: int, end: int) -> bool:
    if start >= end:
        return True

    if text[start] != text[end]:
        return False

    return is_palindrome(text, start + 1, end - 1)


def check_palindrome(text: str) -> bool:
    return is_palindrome(text, 0, len(text) - 1)


s = "banana"

if check_palindrome(s):
    print(f"This is palindrome: {s}")
else:
    print(f"This is not palindrome: {s}")
