class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        self.num = 0
        max_area = -1
        def dfs(grid, i, j):
            for k,v in [(i-1, j),(i+1,j),(i,j-1),(i,j+1)]:
                if k >=0 and v >=0 and k <=n-1 and v <=m-1 and grid[k][v] == 1:
                    grid[k][v] = 0
                    self.num+=1
                    dfs(grid, k, v)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    self.num+=1
                    dfs(grid, i, j)
                if self.num > max_area:
                    max_area = self.num
                self.num = 0
        return max_area
