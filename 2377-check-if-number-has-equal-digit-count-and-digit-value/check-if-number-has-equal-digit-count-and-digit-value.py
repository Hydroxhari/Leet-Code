from collections import Counter

class Solution(object):
    def digitCount(self, n):
        count = Counter(n)  # Count all digits once

        for i, digit in enumerate(n):
            if count[str(i)] != int(digit):
                return False

        return True
