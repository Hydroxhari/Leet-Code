class Solution(object):
    def asteroidCollision(self, a):

        l=[]
        for i in a:
            if i<0:
                while l and l[-1]>0 and l[-1]<-i :
                    l.pop()
                if l and l[-1]==-i:
                    l.pop()
                elif not l or l[-1]<0:
                    l.append(i)
            else:
                l.append(i)
        return l