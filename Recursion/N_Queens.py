def isval(board,r,c,n):
    for i in range(r):
        if board[i][c]=="Q":
            return False
    i=r
    j=c
    while i>-1 and j>-1:
        if board[i][j]=="Q":
            return False
        i-=1
        j-=1
    i=r
    j=c
    while i>-1 and j<n:
        if board[i][j]=="Q":
            return False
        i-=1
        j+=1
    return True
def solve(board,ans,i,n):
    if i==len(board):
        ans.append(["".join(val) for val in board])
        return
    for j in range(n):
        if isval(board,i,j,n):
            board[i][j]="Q"
            solve(board,ans,i+1,n)
            board[i][j]="."
        
def solve_n_queens(n):
    board=[["." for _ in range(n)] for _ in range(n)]
    ans=[]
    solve(board,ans,0,n)
    return ans
print(solve_n_queens(5))