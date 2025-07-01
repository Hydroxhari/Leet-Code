class Solution(object):
    def countGoodSubstrings(self, s):

        c=Counter(s[:3])
        r=0
        if len(c)==3:
            r+=1
        for i in range(3,len(s)):
            c[s[i-3]]-=1
            if c[s[i-3]]==0:
                del c[s[i-3]]
            c[s[i]]+=1
            if len(c)==3:
                r+=1
        return r