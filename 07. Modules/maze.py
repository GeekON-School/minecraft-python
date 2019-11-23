from random import choice


def generate_maze(width, height):
    assert width % 2 == 1 and width > 3
    assert height % 2 == 1 and height > 3
    m = [[1 for _ in range(width)] for _ in range(height)]
    for i in range(1, height, 2):
        for j in range(1, width, 2):
            m[i][j] = -1
    m[1][1] = 0  # start point
    stack = [(1, 1)]
    while len(stack) > 0:
        i, j = stack[-1]
        n = []
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            p = (i + 2 * di, j + 2 * dj)
            if 0 < p[0] < height and 0 < p[1] < width:
                if m[p[0]][p[1]] == -1:
                    n.append((di, dj, p))
        if len(n) == 0:
            stack.pop()
            continue
        di, dj, p = choice(n)
        m[i + di][j + dj] = 0
        m[p[0]][p[1]] = 0
        stack.append(p)

    return m
