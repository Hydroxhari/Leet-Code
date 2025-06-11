class Solution(object):
    def digitCount(self, n):

        for i in range(len(n)):
            if n.count(str(i))!=int(n[i]):
                return False
        return True
