class Solution(object):
    def removeDuplicates(self, n):

        ci=1
        p=0
        for i in range(1,len(n)):
            if n[i]!=n[p]:
                n[ci]=n[i]
                p=i
                ci+=1
        return ci