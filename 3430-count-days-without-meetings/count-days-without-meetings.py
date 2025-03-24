class Solution(object):
    def countDays(self, d, m):
        m.sort(key=lambda x:x[0])
        c=0
        s,e=m[0]
        c+=s-1
        for i in range(1,len(m)):
            cs,ce=m[i]
            if cs>e:
                c+=cs-e-1
                e=ce
            else:
                e=max(ce,e)
        c+=d-e
        return c