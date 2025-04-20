from collections import Counter

class Solution(object):
    def numRabbits(self, answers):
        count = Counter(answers)
        total = 0
        for answer, num in count.items():
            groups = (num + answer) // (answer + 1)
            total += groups * (answer + 1)
        return total
