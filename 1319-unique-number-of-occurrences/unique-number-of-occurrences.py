class Solution(object):
    def uniqueOccurrences(self, a):
        c=Counter(a)
        return len(set(c.values()))==len(c.keys())