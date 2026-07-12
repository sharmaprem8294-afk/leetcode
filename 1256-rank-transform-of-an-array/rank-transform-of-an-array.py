class Solution:
    def arrayRankTransform(self, arr):
        rank = {}

        for i, num in enumerate(sorted(set(arr)), 1):
            rank[num] = i

        return [rank[num] for num in arr]