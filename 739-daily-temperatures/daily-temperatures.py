class Solution(object):
    def dailyTemperatures(self, t):

        a=[]
        s=[]
        for i in range(len(t)-1,-1,-1):
            while s and t[i]>=t[s[-1]]:
                s.pop()
            if s:
                a.append(s[-1]-i)
            else:
                a.append(0)
            s.append(i)
        return a[::-1]
