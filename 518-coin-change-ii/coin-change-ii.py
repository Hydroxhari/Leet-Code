class Solution(object):
    def change(self, a, c):
        n = [0] * (a + 1)
        n[0] = 1

        for coin in c:
            for i in range(coin, a + 1):
                n[i] += n[i - coin]
        return n[-1]
