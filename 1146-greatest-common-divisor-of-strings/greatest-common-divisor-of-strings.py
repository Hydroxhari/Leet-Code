class Solution(object):
    def gcdOfStrings(self, s1, s2):
        if s1 + s2 != s2 + s1:
            return ""
        
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        gcd_len = gcd(len(s1), len(s2))
        return s1[:gcd_len]
