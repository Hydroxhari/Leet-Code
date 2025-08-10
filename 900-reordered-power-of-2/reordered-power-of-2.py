class Solution(object):
    def reorderedPowerOf2(self, n):
        # Sort the digits of n
        n_digits = sorted(str(n))
        
        # Check against all powers of 2 up to 10^9
        for i in range(31):  # 2^30 is the largest power of 2 <= 10^9
            if sorted(str(2**i)) == n_digits:
                return True
        
        return False
