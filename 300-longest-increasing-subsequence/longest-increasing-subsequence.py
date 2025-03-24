class Solution(object):
    def lengthOfLIS(self, arr):
        piles = []

        for num in arr:
            pos = bisect.bisect_left(piles, num)  # Binary search position
            if pos == len(piles):
                piles.append(num)  # New pile
            else:
                piles[pos] = num   # Replace in the existing pile

        return len(piles)