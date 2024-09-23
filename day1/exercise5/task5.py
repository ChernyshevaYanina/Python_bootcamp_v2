def from_str_to_float(s: str) -> float:
    minus: bool = s.startswith('-')
    decimal: bool = False
    decimal_places: int = 0
    if minus:
        s = s.replace('-', '')
    result: float = 0

    for char in s:
        if char.isdigit():
            digit: int = ord(char) - ord('0')
            if decimal:
                result = result * 10 + digit
                decimal_places += 1
            else:
                result = result * 10 + digit
        elif char == '.':
            decimal = True
        else:
            raise ValueError

    if minus:
        result = -result

    return result / (10 ** decimal_places)


def multiply(a: float) -> float:
    return a * 2


def main() -> None:
    s: str = input()
    try:
        print(multiply(from_str_to_float(s)))
    except ValueError:
        print('Invalid input')


if __name__ == '__main__':
    main()
