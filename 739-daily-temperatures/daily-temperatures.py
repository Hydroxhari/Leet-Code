class Solution(object):
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        res = [0] * n
        hottest = temperatures[n-1]
        for i in range(n-2, -1, -1):
            if temperatures[i] >= hottest:
                hottest = temperatures[i]
                continue
            days = 1
            while temperatures[i+days] <= temperatures[i]:
                days += res[i+days]
            res[i] = days
        return res
    