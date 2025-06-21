class Solution(object):
    def minimumDeletions(self, word, k):
        freq = list(Counter(word).values())
        freq.sort()
        n = len(freq)
        result = float('inf')

        for i in range(n):
            base = freq[i]
            deletions = 0

            # All frequencies before index i are < base, so delete all
            deletions += sum(freq[:i])

            # All frequencies > base + k: reduce extras
            for j in range(i, n):
                if freq[j] > base + k:
                    deletions += freq[j] - (base + k)

            result = min(result, deletions)

        return result