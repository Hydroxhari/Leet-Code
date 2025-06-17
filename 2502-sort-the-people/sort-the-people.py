class Solution(object):
    def sortPeople(self, names, heights):
        # Combine names and heights, sort by height in descending order
        people = zip(names, heights)
        sorted_people = sorted(people, key=lambda x: -x[1])
        return [name for name, height in sorted_people]
