def derivative(degree: int, point: float,
               coef1: float, coef2: float, coef3: float) -> float:
    match degree:
        case 0:
            return 0.0
        case 1:
            return coef1
        case 2:
            return coef1 * 2 * point + coef2
        case 3:
            return coef1 * 3 * point**2 + 2 * coef2 * point + coef3
        case _:
            return coef1 * degree * point**(degree-1) + \
                coef2 * (degree-1) * point**(degree-2) + \
                coef3 * (degree-2) * point**(degree-3)


def main():
    degree, point = map(float, input().split())
    coef1 = float(input())
    coef2 = float(input())
    coef3 = float(input())

    result = derivative(degree, point, coef1, coef2, coef3)
    print(f"{result:.3f}")


if __name__ == "__main__":
    main()
