class Solution(object):
    def maxVowels(self, s, k):
        c=0
        for i in range(k):
            if s[i] in {'a','e','i','o','u'}:
                c+=1
        m=c
        for i in range(k,len(s)):
            if s[i-k] in {'a','e','i','o','u'}:
                c-=1
            if s[i] in {'a','e','i','o','u'}:
                c+=1
            m=max(m,c)
        return m
        