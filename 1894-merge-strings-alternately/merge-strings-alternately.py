class Solution(object):
    def mergeAlternately(self, q, w):

        i,j=0,0
        s=''
        while i<max(len(q),len(w)):
            if i<len(q):
                s+=q[i]
            if i<len(w):
                s+=w[i]
            i+=1
        return s