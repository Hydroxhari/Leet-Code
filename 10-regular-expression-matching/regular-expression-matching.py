class Solution(object):
    def isMatch(self, s, p):
        from functools import lru_cache

        @lru_cache(None)
        def bt(i, j):
            if j == len(p):
                return i == len(s)

            first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')

            if j + 1 < len(p) and p[j+1] == '*':
                # two choices: skip the "x*" or use it if first_match
                return bt(i, j+2) or (first_match and bt(i+1, j))
            else:
                return first_match and bt(i+1, j+1)

        return bt(0, 0)
