class NumArray(object):

    def __init__(self, nums):
        self.s=[]
        a=0
        for i in nums:
            a+=i
            self.s.append(a)

    def sumRange(self, l, r):
        if l==0:
            return self.s[r]
        return self.s[r] - self.s[l-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)