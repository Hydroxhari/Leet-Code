class Solution(object):
    def isAnagram(self, s, t):
        from collections import Counter
        return Counter(s)==Counter(t)