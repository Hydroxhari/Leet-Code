class Solution(object):
    def majorityElement(self, n):

        n.sort()
        return(n[len(n)/2])