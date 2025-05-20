class Solution(object):
    def isZeroArray(self, nums, queries):

        temp = [0] * (len(nums) + 1)
        for q1, q2 in queries:
            temp[q1] += 1
            temp[q2 + 1] -= 1
        cur = 0
        # print(temp)
        for i in range(len(nums)):
            cur += temp[i]
            if cur < nums[i]:
                return False
        return True