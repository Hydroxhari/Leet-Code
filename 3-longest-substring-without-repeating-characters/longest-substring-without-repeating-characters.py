class Solution(object):
    def lengthOfLongestSubstring(self, s):

        seen=set()
        m=0
        cl=0
        l=0

        for i in s:
            while i in seen:
                seen.remove(s[l])
                cl-=1
                l+=1
            seen.add(i)
            cl+=1
            m=max(m,cl)
        return m