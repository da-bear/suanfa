"""
    给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
    岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
    此外，你可以假设该网格的四条边均被水包围。
    输入：grid = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ]
    输出：1
"""

from collections import deque


def numIslands(grid):
    """
    二维数组水平方向为y轴，垂直向下为x轴
    """
    # 岛屿数量
    count = 0
    m = len(grid)
    n = len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1":
                count += 1
                dfs(grid, i, j)
    return count


def dfs(grid, i, j):
    """
    将i，j 代表的区域变为0 ----> 会超时
    """
    q = deque()
    q.append((i, j))
    while len(q) > 0:
        (x, y) = q.popleft()
        grid[x][y] = "0"
        if x - 1 >= 0 and grid[x - 1][y] == "1":
            q.append((x - 1, y))
        if y - 1 >= 0 and grid[x][y - 1] == "1":
            q.append((x, y - 1))
        if x + 1 <= len(grid) - 1 and grid[x + 1][y] == "1":
            q.append((x + 1, y))
        if y + 1 <= len(grid[0]) - 1 and grid[x][y + 1] == "1":
            q.append((x, y + 1))


def dfs2(grid, i, j):
    """
    使用递归遍历框架处理
    """
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != "1":
        return
    grid[i][j] = "0"
    dfs2(grid, i - 1, j)
    dfs2(grid, i, j - 1)
    dfs2(grid, i + 1, j)
    dfs2(grid, i, j + 1)
