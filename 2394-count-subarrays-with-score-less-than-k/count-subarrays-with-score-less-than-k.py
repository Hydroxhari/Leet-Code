class Solution(object):
    def countSubarrays(self, n, k):
        s = 0
        j = 0
        c = 0

        for i in range(len(n)):
            s += n[i]
            while j <= i and s * (i - j + 1) >= k:
                s -= n[j]
                j += 1

            c += (i - j + 1)

        return c
