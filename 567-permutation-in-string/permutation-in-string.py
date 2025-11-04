class Solution(object):
    def checkInclusion(self, s1, s2):

        a=len(s1)
        b=len(s2)
        if a>b:
            return False
        c=Counter(s1)
        l=Counter(s2[:a])

        def dp(l):
            return all(l[i]==j for i,j in c.items())

        if dp(l):
            return True
        for i in range(a,b):
            l[s2[i-a]]-=1
            l[s2[i]]+=1
            if dp(l):
                return True
        return False
