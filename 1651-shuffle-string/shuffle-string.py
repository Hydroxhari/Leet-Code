class Solution(object):
    def restoreString(self, s, indices):
        n = len(s)
        newLength = [''] * n
        
        for i in range(n):
            newLength[indices[i]] = s[i]
            
        return "".join(newLength)