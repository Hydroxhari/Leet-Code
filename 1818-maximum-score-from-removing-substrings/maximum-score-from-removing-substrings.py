class Solution(object):
    def maximumGain(self, s, x, y):
        def remove(s, a, b, score):
            stack = []
            total = 0
            for ch in s:
                if stack and stack[-1] == a and ch == b:
                    stack.pop()
                    total += score
                else:
                    stack.append(ch)
            return total, "".join(stack)

        if x >= y:
            gain1, rest = remove(s, 'a', 'b', x)
            gain2, _ = remove(rest, 'b', 'a', y)
        else:
            gain1, rest = remove(s, 'b', 'a', y)
            gain2, _ = remove(rest, 'a', 'b', x)

        return gain1 + gain2
