class Solution(object):
    def countGoodNumbers(self, n):
        mod = 10**9 + 7

        def power(x, y):
            result = 1
            x = x % mod
            while y > 0:
                if y % 2 == 1:
                    result = (result * x) % mod
                y = y // 2
                x = (x * x) % mod
            return result

        even_positions = (n + 1) // 2
        odd_positions = n // 2

        return (power(5, even_positions) * power(4, odd_positions)) % mod
