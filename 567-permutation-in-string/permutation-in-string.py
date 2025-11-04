from collections import Counter

class Solution(object):
    def checkInclusion(self, s1, s2):
        a, b = len(s1), len(s2)
        if a > b:
            return False

        c = Counter(s1)
        l = Counter(s2[:a])

        if c == l:
            return True

        for i in range(a, b):
            l[s2[i]] += 1
            l[s2[i - a]] -= 1
            if l[s2[i - a]] == 0:
                del l[s2[i - a]]
            if l == c:
                return True

        return False
