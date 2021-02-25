class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        n = len(board)
        if not n:
            return 0 
        m = len(board[0])

        def dfs(board, i, j):
            if i<=n-1 and j<=m-1 and i>=0 and j>=0 and board[i][j] == 'O':
                board[i][j] = 'A'
                for k,v in [(i-1, j),(i+1, j),(i,j+1),(i,j-1)]:
                    dfs(board, k, v)
        for i in range(m):
            if board[0][i] == 'O':
                board[0][i] = 'A'
                for k, v in [(1, i), (0, i+1)]:
                    dfs(board, k, v)
            if board[-1][i] == 'O':
                board[-1][i] = 'A'
                for k, v in [(n-2, i), (n-1, i+1)]:
                    dfs(board, k, v)

        for i in range(1, n-1):
            if board[i][0] == 'O':
                board[i][0] = 'A'
                for k, v in [(i, 1), (i+1, 0)]:
                    dfs(board, k, v)
            if board[i][-1] == 'O':
                board[i][-1] = 'A'
                for k, v in [(i, m-2), (i+1, m-1)]:
                    dfs(board, k, v)
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'A':
                    board[i][j] = 'O'
