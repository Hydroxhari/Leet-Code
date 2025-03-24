class Solution(object):
    def jump(self, n):

        d=0
        c=0
        j=0
        for i in range(len(n)-1):
            d=max(d,i+n[i])
            if i==c:
                j+=1
                c=d

                if c>=len(n)-1:
                    break
        return j
        