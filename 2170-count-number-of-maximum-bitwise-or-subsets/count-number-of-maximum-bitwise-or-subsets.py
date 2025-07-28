class Solution(object):
    def countMaxOrSubsets(self, nums):
        dp = [0] * (1 << 17)
        dp[0] = 1
        max_or = 0

        for num in nums:
            for i in range(max_or, -1, -1):
                dp[i | num] += dp[i]
            max_or |= num

        return dp[max_or] 