class Solution(object):
    def lengthOfLongestSubstring(self, s):

        l=set()
        j=0
        m=0
        for i in range(len(s)):
            while s[i] in l:
                l.remove(s[j])
                j+=1
            l.add(s[i])
            m=max(m,i-j+1)
        return m