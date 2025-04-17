class Solution(object):
    def reversePrefix(self, w, c):
        if c in w:
            i = w.index(c)
            if i == len(w):
                return reversed(w)
            w=''.join(reversed(w[:i+1]))+w[i+1:]
        return w

        