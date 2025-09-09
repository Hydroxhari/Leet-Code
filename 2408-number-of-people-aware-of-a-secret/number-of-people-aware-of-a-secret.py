class Solution(object):
    def peopleAwareOfSecret(self, n, delay, forget):
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        dp[1] = 1
        share = 0  # people available to share

        for day in range(2, n + 1):
            # Add people who become eligible to share today
            if day - delay >= 1:
                share = (share + dp[day - delay]) % MOD
            # Remove people who forget today
            if day - forget >= 1:
                share = (share - dp[day - forget]) % MOD
            # People learning the secret today
            dp[day] = share

        # People who still remember on day n
        ans = 0
        for i in range(n - forget + 1, n + 1):
            ans = (ans + dp[i]) % MOD
        return ans
