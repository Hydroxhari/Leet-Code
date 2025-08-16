class Solution(object):
    def solveNQueens(self, n):

        l=[]

        def ip(i,j,b):
            for x in range(i):
                if b[x][j]=='Q':
                    return False
            
            for x,y in [(-1,-1),(1,1),(-1,1),(1,-1)]:
                ni,nj=i+x,j+y
                while 0<=ni<n and 0<=nj<n:
                    if b[ni][nj]=='Q':
                        return False
                    ni+=x
                    nj+=y
            return True
        
        def bt(i,b):
            if i==n:
                cl=[]
                for x in b:
                    cl.append(''.join(x))
                l.append(cl)
            
            for j in range(n):
                if ip(i,j,b):
                    b[i][j]='Q'
                    bt(i+1,b)
                    b[i][j]='.'
            
        
        b=[['.' for _ in range(n)]for _ in range(n)]
        print(b)
        bt(0,b)

        return l