class Solution(object):
    def kthSmallestProduct(self, nums1, nums2, k):
        A1 = sorted([- x for x in nums1 if x < 0])
        A2 = [x for x in nums1 if x >= 0]
        B1 = sorted([-x for x in nums2 if x < 0])
        B2 = [x for x in nums2 if x >= 0]

        neg = len(A1)*len(B2) + len(A2)*len(B1)
        if k <= neg:
            k = neg - k + 1
            B1 , B2 = B2 , B1
            sign = -1 

        else :
            k -= neg
            sign =+ 1

        def count_le(A , B, t):
            count = 0
            j = len(B) - 1
            for x in A :
                while j >= 0 and x * B[j] > t:
                    j -= 1
                count += (j+1)
            return count

        lo , hi = 0 , 10**10
        while lo < hi:
            mid = (lo + hi)// 2
            if count_le(A1 ,B1 ,mid) + count_le(A2 , B2 , mid) >= k:
                hi = mid
            else :
                lo = mid + 1
        return lo * sign       