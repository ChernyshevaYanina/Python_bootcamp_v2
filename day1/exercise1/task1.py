def scalar_sum() -> float:
    vector1: list[float] = [float(x) for x in input().split()]
    vector2: list[float] = [float(x) for x in input().split()]
    return sum(map(lambda a, b: a * b, vector1, vector2))


def main():
    print(scalar_sum())


if __name__ == '__main__':
    main()
