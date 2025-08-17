class Solution(object):
    def mergeAlternately(self, a, b):

        s=''
        m=min(len(a),len(b))
        for i in range(m):
            s+=a[i]+b[i]
        if m<len(a):
            s+=a[m:]
        if m<len(b):
            s+=b[m:]
        return s