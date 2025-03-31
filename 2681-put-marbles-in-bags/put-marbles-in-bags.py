class Solution(object):
    def putMarbles(self, weights, k):
        if k == 1:
            return 0  # If we have only one bag, the score is fixed.

        # Step 1: Compute pairwise sums
        pairwise_sums = [weights[i] + weights[i+1] for i in range(len(weights) - 1)]
        
        # Step 2: Find max and min score using k-1 cuts
        max_score = sum(nlargest(k-1, pairwise_sums))
        min_score = sum(nsmallest(k-1, pairwise_sums))
        
        return max_score - min_score
            