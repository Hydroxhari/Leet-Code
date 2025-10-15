class Solution(object):
    def rotate(self, n, k):

        l=[1]*len(n)
        for i in range(len(n)):
            l[(i+k)%len(n)]=n[i]
        n[:]=l[:]

        