class Solution(object):
    def insert(self, l, n):

        r=[]

        st,et=n[0],n[1]

        i=0
        while i<len(l):
            cs,ce=l[i][0],l[i][1]
            if ce<st or cs>et:
                r.append([cs,ce])
            else:
                st=min(cs,st)
                et=max(ce,et)
            i+=1
            
        r.append([st,et])
        return sorted(r)