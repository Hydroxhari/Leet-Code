class FenwickTree:
    def __init__(self, size):
        self.size = size + 2
        self.tree = [0] * self.size

    def update(self, index, value):
        index += 1  # 1-based indexing
        while index < self.size:
            self.tree[index] += value
            index += index & -index

    def query(self, index):
        index += 1  # 1-based indexing
        result = 0
        while index > 0:
            result += self.tree[index]
            index -= index & -index
        return result


class Solution(object):
    def goodTriplets(self, n, n2):
        h = {val: idx for idx, val in enumerate(n2)}
        mapped = [h[val] for val in n]
        max_val = len(n)

        left_tree = FenwickTree(max_val)
        right_tree = FenwickTree(max_val)

        # Initialize right_tree with all counts
        for val in mapped:
            right_tree.update(val, 1)

        total = 0

        for j in range(len(mapped)):
            current = mapped[j]
            right_tree.update(current, -1)  # remove current element from right

            left_count = left_tree.query(current - 1)  # elements less than current
            right_count = right_tree.query(max_val - 1) - right_tree.query(current)  # elements greater than current

            total += left_count * right_count

            left_tree.update(current, 1)  # add current element to left

        return total