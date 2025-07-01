class Solution(object):
    def possibleStringCount(self, w):

        l=[]
        c=1

        for i in range(len(w)-1):
            if w[i]==w[i+1]:
                c+=1
            else:
                l.append(c)
                c=1
        l.append(c)
        
        cs=1
        for i in l:
            if i>1:
                cs+=i-1
        return cs

