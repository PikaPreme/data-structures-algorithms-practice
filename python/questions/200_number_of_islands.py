# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#
#
#
# Example 1:
#
# Input: grid = [
#     ["1","1","1","1","0"],
#     ["1","1","0","1","0"],
#     ["1","1","0","0","0"],
#     ["0","0","0","0","0"]
# ]
# Output: 1
#
# Example 2:
#
# Input: grid = [
#     ["1","1","0","0","0"],
#     ["1","1","0","0","0"],
#     ["0","0","1","0","0"],
#     ["0","0","0","1","1"]
# ]
# Output: 3
#

# naive methodology: traverse through the list, and check to see if an index is an island (1).
# if the index is an island, we'll perform a BFS search on the vertical and horizontal indexes.

# mark all visited indexes in list by saving it's index, or modifying the value
# if the indexes of the array < 0 or greater than the max, it's out of bounds. or if they're visited (marked) or in visited array. Means we've visited the node.
# else if we havn't visited it, and it's a 1, we'll do bfs again

class Solution(object):
    def numIslands(self, grid):
        count = 0
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i,j)
                    count += 1
        return count

    def dfs(self, grid, i,j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':      # if we're out of bounds, or not an island
            return
        grid[i][j] = '#'                     # mark node visited
        self.dfs(grid, i-1, j)         # do a dfs on each adjacent node if it's an island (1)
        self.dfs(grid, i+1, j)
        self.dfs(grid, i, j-1)
        self.dfs(grid, i, j+1)

