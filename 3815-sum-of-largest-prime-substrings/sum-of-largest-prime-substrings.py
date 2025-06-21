from functools import lru_cache

class Solution(object):
    def sumOfLargestPrimes(self, s):
        @lru_cache(None)
        def is_prime(n):
            if n <= 1:
                return False
            if n <= 3:
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False
            for i in range(5, int(n**0.5) + 1, 6):
                if n % i == 0 or n % (i + 2) == 0:
                    return False
            return True

        u = set()
        n = len(s)

        for i in range(n):
            if s[i] == '0':
                continue  # Skip substrings starting with 0
            for j in range(i, n):  # Limit to max 9-digit substrings
                num = int(s[i:j + 1])
                if is_prime(num):
                    u.add(num)

        top_primes = sorted(u, reverse=True)
        return sum(top_primes[:3])
