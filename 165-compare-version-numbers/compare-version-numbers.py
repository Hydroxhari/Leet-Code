class Solution(object):
    def compareVersion(self, v1, v2):

        l1=list(map(int,v1.split('.')))
        l2=list(map(int,v2.split('.')))
        le1=len(l1)
        le2=len(l2)
        if le1>le2:
            l2.extend([0]*(le1-le2))
        else:
            l1.extend([0]*(le2-le1))
        
        for i in range(max(le1,le2)):
            if l1[i]>l2[i]:
                return 1
            elif l2[i]>l1[i]:
                return -1
        return 0
