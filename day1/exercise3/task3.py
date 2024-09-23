from collections import deque


def count_figures(matrix: list[list[int]]) -> tuple[int, int]:
    squares: int = 0
    circles: int = 0
    rows, cols = len(matrix), len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                queue: deque = deque([(i, j)])
                matrix[i][j] = 0 
                size: int = 1
                min_x, max_x, min_y, max_y = i, i, j, j

                while queue:
                    x, y = queue.popleft()
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < rows and 0 <= ny < cols and \
                            matrix[nx][ny] == 1:
                            matrix[nx][ny] = 0
                            queue.append((nx, ny))
                            size += 1
                            min_x, max_x = min(min_x, nx), max(max_x, nx)
                            min_y, max_y = min(min_y, ny), max(max_y, ny)

                if size > 1:
                    if (max_x - min_x + 1) * (max_y - min_y + 1) == size:
                        squares += 1
                    else:
                        circles += 1

    return squares, circles


def main():
    with open('input.txt', 'r') as f:
        matrix: list[list[int]] = [
            [int(num) for num in line.split()] for line in f.readlines()]

    squares, circles = count_figures(matrix)
    print(squares, circles)


if __name__ == "__main__":
    main()
