class Solution(object):
    def robotWithString(self, s):
        from collections import Counter

        count = Counter(s)
        stack = []
        result = []
        min_char = 'a'

        for c in s:
            stack.append(c)
            count[c] -= 1

            # Update min_char
            while min_char <= 'z' and count[min_char] == 0:
                min_char = chr(ord(min_char) + 1)

            # Greedily pop from stack if it's ≤ current min_char
            while stack and stack[-1] <= min_char:
                result.append(stack.pop())

        return ''.join(result)
