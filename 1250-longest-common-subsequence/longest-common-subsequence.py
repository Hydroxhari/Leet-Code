class Solution:
    def longestCommonSubsequence(self, a: str, b: str) -> int:

        @lru_cache(None)
        def dp(i,j):
            if i==len(a) or j==len(b):
                return 0
            
            nt=max(dp(i+1,j),dp(i,j+1))

            t=0
            if a[i]==b[j]:
                t=1+dp(i+1,j+1)
            
            return max(nt,t)

        
        return dp(0,0)
        