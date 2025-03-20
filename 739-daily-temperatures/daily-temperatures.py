class Solution(object):
    def dailyTemperatures(self, t):
        s=[]
        r=[0]*len(t)

        for i in range(len(t)):
            while s and t[s[-1]]<t[i]:
                p=s.pop()
                r[p]=i-p
            s.append(i)
        return r