class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)#hang
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1
        # canarrive = True
        for i in range(1, n):
            if obstacleGrid[0][i] == 1:
                break 
            dp[0][i] = 1  
        for i in range(1, m):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1
        for i in range(1, m):
            for s in range(1, n):
                if obstacleGrid[i][s] == 1:
                    continue
                dp[i][s] = dp[i-1][s]+dp[i][s-1]
        
        return dp[-1][-1]
