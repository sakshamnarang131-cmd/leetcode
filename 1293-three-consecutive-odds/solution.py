class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        count = 0
        i = 0
        while i<len(arr):
            if arr[i] %2 == 0:
                count = 0
                i-=count
            else:
                count +=1
            if count == 3:
                return True
            i+=1
        return False
