class Solution(object):
    def longestConsecutive(self, n):
        s = set(n)
        longest = 0

        for i in s:
            if i - 1 not in s:  # anchor: sequence start
                current = i
                streak = 1

                while current + 1 in s:
                    current += 1
                    streak += 1

                longest = max(longest, streak)
        
        return longest
