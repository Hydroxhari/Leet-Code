class Solution(object):
    def mergeAlternately(self, a, b):

        s=''

        for i in range(min(len(a),len(b))):
            s+=a[i]+b[i]
        
        if len(a)>len(b):
            s+=a[i+1:]
        elif len(b)>len(a):
            s+=b[i+1:]
        
        return s
