class Solution(object):
    def makeFancyString(self, s):

        l=[]
        c=1
        for i in s:
            if l and l[-1]==i:
                c+=1
            else:
                c=1
            
            if c<3:
                l.append(i)
        return ''.join(l)
