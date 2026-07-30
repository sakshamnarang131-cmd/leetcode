class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        count = 0
        for i in range(len(arr)):
            if arr.count(arr[i]) == 1:
                count +=1
            if count == k:
                return arr[i]
        return ""
