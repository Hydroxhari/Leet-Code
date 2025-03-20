class Solution(object):
    def dailyTemperatures(self, t):
        s=[]
        r=[]

        for i in range(len(t)-1,-1,-1):
            while s and t[s[-1]]<=t[i]:
                s.pop()
            if not s:
                r.append(0)
            else:
                r.append(s[-1]-i)
            s.append(i)
        return r[::-1]