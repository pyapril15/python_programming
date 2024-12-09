def fibonacci(n: int) -> int:
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_list(term: int) -> list:
    return [fibonacci(i) for i in range(n_term)]


n_term = 10
print(fibonacci_list(n_term))
