class Solution(object):
    def checkValidString(self, s):
        o = 0  # Minimum open brackets count (could treat '*' as ')')
        c = 0  # Maximum open brackets count (treat '*' as '(')

        for ch in s:
            if ch == '(':
                o += 1
                c += 1
            elif ch == ')':
                o -= 1
                c -= 1
            else:  # ch == '*'
                o -= 1  # if '*' acts as ')'
                c += 1  # if '*' acts as '('

            if c < 0:
                return False  # Too many closing brackets

            if o < 0:
                o = 0  # Clamp lower bound to 0

        return o == 0
