class Solution(object):
    def findAndReplacePattern(self, w, p):

        c=Counter(p)

        def iso(a,b):

            d={}
            h={}
            for i in range(len(a)):
                if  a[i] not in d :
                    d[a[i]]=b[i]
                if b[i] not in h:
                    h[b[i]]=a[i]
                if d[a[i]]!=b[i] or h[b[i]]!=a[i]:
                    return False
            return True

        l=[]

        for i in w:
            if iso(i,p):
                l.append(i)

        return l

        