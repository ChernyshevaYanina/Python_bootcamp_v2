from typing import Tuple, Deque
from collections import deque


def calculate_max_coins(field: Tuple[Tuple[int, ...]]) -> int:
    n, m = len(field), len(field[0])
    queue: Deque[Tuple[int, int, int]] = deque([(0, 0, field[0][0])])
    max_coins: int = field[0][0]

    while queue:
        i, j, coins = queue.popleft()

        if i == n-1 and j == m-1:
            max_coins = max(max_coins, coins)
            continue

        if i+1 < n:
            queue.append((i+1, j, coins + field[i+1][j]))

        if j+1 < m:
            queue.append((i, j+1, coins + field[i][j+1]))

    return max_coins


def main() -> None:
    n, m = map(int, input().split())
    field: Tuple[Tuple[int, ...]] = tuple(
        tuple(map(int, input().split())) for _ in range(n))

    print(calculate_max_coins(field))


if __name__ == '__main__':
    main()
