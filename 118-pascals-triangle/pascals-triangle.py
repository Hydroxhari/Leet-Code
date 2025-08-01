class Solution(object):
    def generate(self, n):
        l=[]
        for i in range(n):
            r=[1]*(i+1)
            for j in range(1,i):
                r[j]=l[i-1][j-1]+l[i-1][j]
            l.append(r)
        return(l)


        
        