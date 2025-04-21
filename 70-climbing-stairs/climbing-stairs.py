class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        a, b = 1, 2  # base cases for 1 and 2 steps
        for i in range(3, n + 1):
            a, b = b, a + b  # Update for the next step
        return b
