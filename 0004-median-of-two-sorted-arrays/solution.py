class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        temp = nums1 + nums2
        num = sorted(temp)
        n = len(num)
        if (n %2 == 0):
            return (num[n/2] + num[(n/2) - 1])/2.0
        else:
            return num[(n-1)/2]
