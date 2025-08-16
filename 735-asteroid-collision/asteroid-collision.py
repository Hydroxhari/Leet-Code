class Solution(object):
    def asteroidCollision(self, a):

        s=[]
        for i in a:
            if i<0:
                while s and s[-1]>0 and s[-1]<-i:
                    s.pop()
                if s and s[-1]==-i:
                    s.pop()
                    continue
                if not s or s[-1]<0:
                    s.append(i)
            else:
                s.append(i)
        return s