class Solution(object):
    def evalRPN(self, t):
        s=[]
        for i in t:
            if i in {'+', '-', '*', '/'}:
                r=0
                b=int(s.pop())
                a=int(s.pop())
                if i=='+':
                    r=a+b
                elif i=='-':
                    r=a-b
                elif i=='*':
                    r=a*b
                else:
                    r=int(float(a)/b)
                s.append(r)
            else:
                s.append(i)
        return int(s[-1])

        