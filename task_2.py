import re
from decimal import Decimal
from collections.abc import Callable, Generator


# Returns a generator of real numbers found in the input text.
def generator_numbers(text: str) -> Generator[str, None, None]:
    # Find all real numbers in the text
    pattern = r"\s\d+\.\d{2}\s"
    matches = re.findall(pattern, text)

    # Generator to yield floats as strings
    for number in matches:
        yield number.strip()


# Calculate the sum of profits from the text using the provided generator function.
def sum_profit(text: str, func: Callable[[str], Generator[str, None, None]]) -> float:
    generator = func(text)

    profit = Decimal("0")
    for number in generator:
        profit += Decimal(number)

    return profit


def main() -> None:
    text = "1111.00 Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")


if __name__ == "__main__":
    main()
