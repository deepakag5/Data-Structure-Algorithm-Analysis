# Iterative
def hasPathIterative(maze, start, destination):
    if start[0] == destination[0] and start[1] == destination[1]:
        return True

    seen = set()
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    stack = [start]

    while stack:
        i, j = stack.pop()

        for dx, dy in dirs:
            x, y = i, j

            while 0 <= x + dx < len(maze) and 0 <= y + dy < len(maze[0]) and maze[x + dy][y + dy] != 1:
                x, y = x + dx, y + dy

            if [i, j] == destination:
                return True

            if (x, y) not in seen:
                seen.add((x, y))
                stack.append((x, y))

    return False


# Recursive
def hasPathRecursive(maze, start, destination):
    if start[0] == destination[0] and start[1] == destination[1]:
        return True

    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    x, y = start[0], start[1]

    for dx, dy in dirs:
        nx = x
        ny = y

        while 0 <= nx + dx < len(maze) and 0 <= ny + dy < len(maze[0]) and maze[nx + dx][ny + dy] != 1:
            nx += dx
            ny += dy

        if maze[nx][ny] != 0:
            continue

        maze[nx][ny] = 2

        if hasPathRecursive(maze, (nx, ny), destination):
            return True

    return False
