class Solution(object):
    def rotate(self, n, k):

        l=len(n)

        na=[1]*l

        for i in range(l):
            na[(i+k)%l]=n[i]
        print(na)
        n[:]=na[:]