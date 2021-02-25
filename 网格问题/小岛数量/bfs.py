#广度优先
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

        q = collections.deque()
        num_island = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    q.append((i, j))
                    num_island += 1

                    while q:
                        row, col = q.popleft()
                        for (k,v) in [(row-1, col), (row+1, col), (row, col+1), (row, col-1)]:
                            if k>=0 and v>=0 and k<=n-1 and v<=m-1 and grid[k][v] == '1':
                                q.append((k,v))
                                grid[k][v] = '0'
        return num_island
      

