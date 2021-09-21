from collections import deque

N = int(input("Enter the grid size:"))
count = 0

grid = []

for i in range(0, N):
    t = list(input().split(','))
    grid.append(t)


# print(grid)


def boundry(r, c):
    if r < 0 or r > (N - 1) or c < 0 or c > (N - 1):

        return False

    else:

        return True


def path(row, col):
    check = []

    for i in range(0, N):
        t = []
        for j in range(0, N):
            t.append(False)
        check.append(t)

    queue = deque()

    check[row][col] = True

    queue.append([row, col])

    directions = {'E': [0, 1], 'W': [0, -1], 'N': [-1, 0], 'S': [1, 0]}

    while queue:

        q = queue.popleft()

        if q[0] == N - 1 and q[1] == N - 1:
            return True

        else:

            after = grid[q[0]][q[1]]

            for i in range(0, len(after)):
                row = q[0] + directions[after[i]][0]
                col = q[1] + directions[after[i]][1]

                if boundry(row, col) and grid[row][col] != 'D' and check[row][col] != True:
                    check[row][col] = True
                    queue.append([row, col])


    else:

        return False


for i in range(0, len(grid)):

    if grid[0][i] != 'D' and path(0, i):
        count += 1

    if i != 0 and grid[i][0] != 'D' and path(i, 0):
        count += 1

print(count)
