class Solution:
    def totalNQueens(self, n: int) -> List[List[str]]:
        def validMove(board,row,col):
            i=col
            while i>=0:
                if board[row][i]:
                    return False
                i-=1
            i=row
            j=col
            while (i>=0 and j>=0):
                if board[i][j]:
                    return False
                i-=1
                j-=1
            i=row
            j=col
            while (i<n and j>=0):
                if board[i][j]:
                    return False
                i+=1
                j-=1
            return True
        def solve(board,col):
            if (col==n):
                res[0]+=1
                return
            for i in range(n):
                if validMove(board,i,col):
                    board[i][col]=1
                    solve(board,col+1)
                    board[i][col]=0
            return
        
        res=[0]
        board=[]
        for i in range(n):
            board.append([])
            for j in range(n):
                board[-1].append(0)
        solve(board,0)
        return res[0]