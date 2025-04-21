class Solution(object):
    def numberOfArrays(self, d, l, u):

        ao=0
        bo=0
        c=0

        for i in d:
            c+=i
            ao=min(c,ao)
            bo=max(c,bo)
        
        u=u-bo
        l=l-ao

        if l>u:
            return 0
        return u-l+1