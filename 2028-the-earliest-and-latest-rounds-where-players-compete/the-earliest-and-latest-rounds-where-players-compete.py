from functools import lru_cache

class Solution:
    def earliestAndLatest(self, n, firstPlayer, secondPlayer):
        first, second = min(firstPlayer, secondPlayer), max(firstPlayer, secondPlayer)

        @lru_cache(None)
        def dfs(players, round_num):
            # Base case: if first and second meet
            if (first, second) in zip(players, reversed(players)):
                return round_num, round_num

            res_min = float('inf')
            res_max = float('-inf')
            m = len(players)
            pairs = []

            i, j = 0, m - 1
            while i <= j:
                if i == j:
                    # Odd middle guy proceeds automatically
                    pairs.append([[players[i]]])
                else:
                    a, b = players[i], players[j]
                    if (a == first and b == second) or (a == second and b == first):
                        # They are facing each other
                        return round_num, round_num
                    elif a in (first, second):
                        pairs.append([[a]])  # a wins
                    elif b in (first, second):
                        pairs.append([[b]])  # b wins
                    else:
                        # Try both outcomes
                        pairs.append([[a], [b]])
                i += 1
                j -= 1

            # Cartesian product of all winners from each match
            from itertools import product
            for combo in product(*pairs):
                next_round = tuple(sorted(x[0] for x in combo))  # flatten & sort
                mn, mx = dfs(next_round, round_num + 1)
                res_min = min(res_min, mn)
                res_max = max(res_max, mx)

            return res_min, res_max

        return list(dfs(tuple(range(1, n + 1)), 1))
