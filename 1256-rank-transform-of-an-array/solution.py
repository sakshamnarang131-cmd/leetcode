class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        unique_sorted = sorted(list(set(arr)))
        rank = {}
        r=1
        for i in unique_sorted:
            rank[i] = r
            r+=1
        result = []
        for num in arr:
            result.append(rank[num])
        return result
