# Time: O(mn)
# Space:
# Input Space: O(mn)
# Auxiliary Space: O(depth) => O(mn * memory for each call) => O(mn)
#  - O(mn * memory for each call): For call-stack, in the worst
# case, it could be all 1s. Each recursive call might take some
# more space.

# Total Space  O(mn)


def numIslands(self, grid):
    if not grid:
        return 0

    row = len(grid)
    col = len(grid[0])

    count = 0

    # for every element in the matrix, check all its adjacent elements
    for i in range(row):
        for j in range(col):
            if grid[i][j] == '1':
                self.dfs(grid, i, j)
                count += 1

    return count


def dfs(self, grid, i, j):
    # boundary case for matrix
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
        return

    # mark the cell as visited (can assign any except for 1)
    grid[i][j] = '2'

    # make recursive calls in all four adjacent directions
    self.dfs(grid, i + 1, j)
    self.dfs(grid, i - 1, j)
    self.dfs(grid, i, j - 1)
    self.dfs(grid, i, j + 1)
