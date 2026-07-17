class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        n = len(height)
        j = n-1
        max_volume = 0
        while i<j:
            volume = (j-i) * min(height[i], height[j])
            if volume > max_volume:
                max_volume = volume
            if height[i] < height[j]:
                i+=1
            else:
                j-=1
        return max_volume
