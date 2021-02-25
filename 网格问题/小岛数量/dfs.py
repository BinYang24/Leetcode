#深度优先
'''					
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        if n == 0:
            return 0
        m = len(grid[0])
        count = 0
        def dfs(grid, i, j):
            for (k, v) in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if k<=n-1 and v<=m-1 and k>=0 and v>=0 and grid[k][v] == '1':
                    grid[k][v] = '0'
                    dfs(grid, k, v)
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    count+=1
        return count


    	
