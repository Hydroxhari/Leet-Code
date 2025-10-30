class Solution(object):
    def threeSum(self, n):

        n.sort()
        r=[]
        for i in range(len(n)-2):
            if i>0 and n[i]==n[i-1]:
                continue
            j=i+1
            k=len(n)-1
            while j<k:
                s= n[i]+n[j]+n[k]
                if s==0:
                    r.append([n[i],n[j],n[k]])
                    j+=1
                    k-=1
                    while j<k and n[j]==n[j-1]:
                        j+=1
                    while j<k and n[k]==n[k+1]:
                        k-=1
                elif s<0:
                    j+=1
                else:
                    k-=1
        return r
            
