class Solution:
    def minDistance(self, w: str, t: str) -> int:


        l,k=len(w),len(t)

        @lru_cache(None)
        def dfs(i,j,c):
            if j==k:
                return c + (l-i)
            if i==l:
                return c + (k-j) 
            
            if w[i]!=t[j]:
                c= min( dfs(i+1,j,c+1),
                        dfs(i,j+1,c+1),
                        dfs(i+1,j+1,c+1) )
            else:
                return dfs(i+1,j+1,c)

            return c

        return dfs(0,0,0)