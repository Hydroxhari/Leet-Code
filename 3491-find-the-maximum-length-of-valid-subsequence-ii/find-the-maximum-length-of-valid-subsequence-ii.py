class Solution(object):
    def maximumLength(self, nums, k):
        from collections import defaultdict

        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        res = 1  # at least one element is always a valid subsequence

        for i in range(n):
            for j in range(i):
                rem = (nums[j] + nums[i]) % k
                # If there's already a subsequence ending at j with remainder rem,
                # extend it
                dp[i][rem] = max(dp[i][rem], dp[j][rem] + 1)
            # Also consider new pair starting at i (single element — base case)
            for rem in range(k):
                dp[i][rem] = max(dp[i][rem], 1)

            res = max(res, max(dp[i].values()))
        
        return res
