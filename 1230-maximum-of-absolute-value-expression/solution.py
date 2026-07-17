class Solution(object):
    def maxAbsValExpr(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        n = len(arr1)
        v1 = [arr1[i] + arr2[i] + i for i in range(n)]
        v2 = [arr1[i] + arr2[i] - i for i in range(n)]
        v3 = [arr1[i] - arr2[i] + i for i in range(n)]
        v4 = [arr1[i] - arr2[i] - i for i in range(n)]
        return max((max(v1)-min(v1)),(max(v2)-min(v2)),(max(v3)-min(v3)),(max(v4)-min(v4)))
