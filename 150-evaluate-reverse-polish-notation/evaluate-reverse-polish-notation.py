class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for t in tokens:
            if t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            elif t == "-":
                n2 = stack.pop()
                n1 = stack.pop()
                stack.append(n1 - n2)
            elif t == "/":
                n2 = stack.pop()
                n1 = stack.pop()
                stack.append(int(float(n1) / n2))
                print(stack)
            else:
                stack.append(int(t))
        return stack[-1]