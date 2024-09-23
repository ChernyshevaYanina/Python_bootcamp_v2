def find_unique(n: int) -> int:
    unique: dict = dict()
    for i in range(n):
        digits: int = int(input())
        unique[digits] = i
    return len(unique)


def main() -> None:
    num: int = int(input())
    print(find_unique(num))


if __name__ == '__main__':
    main()
