class Solution(object):
    def groupAnagrams(self, s):

        d=defaultdict(list)
        for i in s:
            n=''.join(sorted(i))
            d[n].append(i)
        return d.values()
