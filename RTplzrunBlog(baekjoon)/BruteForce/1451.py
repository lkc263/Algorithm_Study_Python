import sys

read = sys.stdin.readline

n, m = map(int, read().split())

arr = [[0] * (m + 1)]

for i in range(n):
    arr.append([0] + list(map(int, read().strip())))

sum_rec = [[0] * (m + 1) for _ in range(n + 1)]

# (1, 1)부터 (n, m)까지 각 자리의 총합
for i in range(1, n + 1):
    for j in range(1, m + 1):
        sum_rec[i][j] = arr[i][j] + sum_rec[i - 1][j] + sum_rec[i][j - 1] - sum_rec[i - 1][j - 1]


# 각 자리수 총합을 이용해 (a, b)부터 (n, m)까지 합
def sum_of_rec(x1, y1, x2, y2):
    # print(sum_rec[x2][y2], sum_rec[x1 - 1][y2], sum_rec[x2][y1 - 1], y2)
    return sum_rec[x2][y2] - sum_rec[x1 - 1][y2] - sum_rec[x2][y1 - 1] + sum_rec[x1 - 1][y1 - 1]


result = 0
ans = 0

# (1) 전체 직사각형을 세로로만 분할한 경우
for i in range(1, m - 1):
    for j in range(i + 1, m):
        num1 = sum_of_rec(1, 1, n, i)
        num2 = sum_of_rec(1, i + 1, n, j)
        num3 = sum_of_rec(1, j + 1, n, m)

        if result < num1 * num2 * num3:
            result = num1 * num2 * num3

# (2) 전체 직사각형을 가로로만 분할한 경우
for i in range(1, n - 1):
    for j in range(i + 1, n):
        num1 = sum_of_rec(1, 1, i, m)
        num2 = sum_of_rec(i + 1, 1, j, m)
        num3 = sum_of_rec(j + 1, 1, n, m)

        if result < num1 * num2 * num3:
            result = num1 * num2 * num3

# (3) 전체 세로 분할 후, 우측 가로 분할한 경우
for i in range(1, m):
    for j in range(1, n):
        num1 = sum_of_rec(1, 1, n, i)
        num2 = sum_of_rec(1, i + 1, j, m)
        num3 = sum_of_rec(j + 1, i + 1, n, m)

        if result < num1 * num2 * num3:
            result = num1 * num2 * num3

# (4) 전체 세로 분할 후, 좌측 가로 분할한 경우
for i in range(1, n):
    for j in range(1, m):
        num1 = sum_of_rec(1, 1, i, j)
        num2 = sum_of_rec(i + 1, 1, n, j)
        num3 = sum_of_rec(1, j + 1, n, m)

        if result < num1 * num2 * num3:
            result = num1 * num2 * num3

# (5) 전체 가로 분할 후, 하단 세로 분할한 경우
for i in range(1, n):
    for j in range(1, m):
        num1 = sum_of_rec(1, 1, i, m)
        num2 = sum_of_rec(i + 1, 1, n, j)
        num3 = sum_of_rec(i + 1, j + 1, n, m)

        if result < num1 * num2 * num3:
            result = num1 * num2 * num3

# (6) 전체 가로 분할 후, 상단 세로 분할한 경우
for i in range(1, n):
    for j in range(1, m):
        num1 = sum_of_rec(1, 1, i, j)
        num2 = sum_of_rec(1, j + 1, i, m)
        num3 = sum_of_rec(i + 1, 1, n, m)

        if result < num1 * num2 * num3:
            result = num1 * num2 * num3

print(result)
