class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if not n:
            return 0
        
        m = len(grid[0])
        # overlap = [[0] * m for _ in range(n)]
        num = 0
        overlap = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    num+=1
                    for k,v in [(i-1, j),(i+1,j),(i,j-1),(i,j+1)]:
                        if k >=0 and v >=0 and k <=n-1 and v <=m-1 and grid[k][v] == 1:
                            overlap+=1
        # print(sum(overlap))
        return num*4-overlap
