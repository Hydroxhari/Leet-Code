class Solution(object):
    def kidsWithCandies(self, c, e):

        m=max(c)
        dp=[]
        for i in c:
            if i+e>=m:
                dp.append(True)
            else:
                dp.append(False)
        return dp