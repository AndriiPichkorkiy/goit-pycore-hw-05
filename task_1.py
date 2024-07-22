from collections.abc import Callable


def caching_fibonacci() -> Callable[[int], int]:
    cache = {}

    def fibonacci(n: int) -> int:
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            # If the value is already in the cache, return it
            return cache[n]

        # Сalculate the value, store it in the cache and return it
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


def main() -> None:
    # Get the fibonacci function
    fib = caching_fibonacci()

    # Use the fibonacci function to calculate Fibonacci numbers
    print(fib(10))
    print(fib(15))


if __name__ == "__main__":
    main()
