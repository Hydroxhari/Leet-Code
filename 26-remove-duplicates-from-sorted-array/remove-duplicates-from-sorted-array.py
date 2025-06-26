class Solution(object):
    def removeDuplicates(self, n):

        j=0
        v=set()

        for i in range(1,len(n)):
            if n[i]!=n[j]:
                n[j+1]=n[i]
                j+=1
        
        return j+1

            
