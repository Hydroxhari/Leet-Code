class NumArray(object):

    def __init__(self, nums):
        self.n=nums
        for i in range(1,len(self.n)):
            self.n[i]=self.n[i-1]+self.n[i]
        print(self.n)

    def sumRange(self, left, right):
        if left==0:
            return self.n[right]
        return self.n[right]-self.n[left-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)