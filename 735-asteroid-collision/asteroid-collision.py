class Solution(object):
    def asteroidCollision(self, a):

        s=[]
        for i in a:
            cs=False
            while s and i<0 and s[-1]>0:
                if abs(i)>s[-1]:
                    s.pop()
                elif abs(i)==s[-1]:
                    s.pop()
                    cs=True
                    break
                else:
                    cs=True
                    break
            if not cs:
                s.append(i)
        return s
