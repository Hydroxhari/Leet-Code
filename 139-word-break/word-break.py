class Solution(object):
    def wordBreak(self, s, w):

        memo={}
        def dp(s):
            if not s:
                return True
            if s in memo:
                return memo[s]
            
            isb=False
            for i in w:
                l=len(i)
                if s[:l]==i:
                    isb = isb or dp(s[l:])
            
            memo[s] = isb
            return isb

        return dp(s)