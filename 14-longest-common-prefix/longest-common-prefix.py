class Solution(object):
    def longestCommonPrefix(self, s):

        s.sort(key=lambda x: len(x))
        e=s[0]
        l=len(e)

        for i in s:
            while e and i[:l]!=e:
                e=e[:-1]
                l-=1
        
        return e