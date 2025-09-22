class Solution(object):
    def maxFrequencyElements(self, nums):
        freq = [0] * 101
        mx = 0
        res = 0
        for n in nums:
            freq[n] += 1
            f = freq[n]
            if f > mx:
                mx = f
                res = f
            elif f == mx:
                res += f
        return res