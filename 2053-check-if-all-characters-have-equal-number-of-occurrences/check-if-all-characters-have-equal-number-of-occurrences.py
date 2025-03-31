class Solution(object):
    def areOccurrencesEqual(self, s):
        c=Counter(s)
        if len(set(c.values()))==1:
            return True
        return False