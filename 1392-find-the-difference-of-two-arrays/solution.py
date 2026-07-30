class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        temp = []
        result = []
        for i in range(len(nums1)):
            if nums1[i] not in nums2:
                temp.append(nums1[i])
        result.append(list(set(temp)))
        temp = []
        for i in range(len(nums2)):
            if nums2[i] not in nums1:
                temp.append(nums2[i])
        result.append(list(set(temp)))
        return result
