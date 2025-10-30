from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        r = Counter(t)
        l = Counter()
        res = ''
        left = 0

        for right in range(len(s)):
            l[s[right]] += 1

            # shrink from left while all conditions are satisfied
            while all(l[ch] >= r[ch] for ch in r):
                if not res or len(res) > right - left + 1:
                    res = s[left:right+1]
                l[s[left]] -= 1
                left += 1

        return res
