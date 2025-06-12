class Solution(object):
    def mergeTriplets(self, triplets, target):
        a, b, c = False, False, False  # flags for x, y, z components

        for t in triplets:
            # Ignore triplets that overshoot the target
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue

            # Set flags if current triplet matches target component
            if t[0] == target[0]:
                a = True
            if t[1] == target[1]:
                b = True
            if t[2] == target[2]:
                c = True

        return a and b and c
