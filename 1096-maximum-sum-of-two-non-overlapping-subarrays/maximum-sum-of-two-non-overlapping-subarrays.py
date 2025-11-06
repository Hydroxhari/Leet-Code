class Solution(object):
    def maxSumTwoNoOverlap(self, nums, firstLen, secondLen):
        # Helper: computes max total sum when firstLen window comes before secondLen
        def helper(L, M):
            n = len(nums)
            # prefix sum of first L elements
            sumL = sum(nums[:L])
            sumM = sum(nums[L:L+M])
            maxL = sumL
            result = sumL + sumM

            # slide both windows
            for i in range(L + M, n):
                # move L window by 1
                sumL += nums[i - M] - nums[i - M - L]
                # update best L window so far
                maxL = max(maxL, sumL)
                # move M window by 1
                sumM += nums[i] - nums[i - M]
                # combine current M + best L before it
                result = max(result, maxL + sumM)
            return result

        # Try both orders: (first before second) and (second before first)
        return max(helper(firstLen, secondLen), helper(secondLen, firstLen))
