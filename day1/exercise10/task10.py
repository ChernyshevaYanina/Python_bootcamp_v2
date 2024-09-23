from typing import List, Tuple


def find_minimum_cost_apparats(N: int, total_time: int) -> int:
    apparats: List[Tuple[int, int, int]] = []
    for _ in range(N):
        year, cost, time = map(int, input().split())
        apparats.append((year, cost, time))

    apparats.sort(key=lambda x: (x[0], x[1], x[2]))

    for i in range(N):
        for j in range(i+1, N):
            if apparats[i][0] == apparats[j][0] and apparats[i][2] \
                    + apparats[j][2] == total_time:
                return apparats[i][1] + apparats[j][1]

    return ""


def main():
    N: int
    total_time: int
    try:
        N, total_time = map(int, input().split())
        result: int = find_minimum_cost_apparats(N, total_time)
        print(result)
    except:
        print("Invalid input")


if __name__ == "__main__":
    main()
