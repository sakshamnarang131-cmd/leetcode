class Solution(object):
    def minimumChairs(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_chairs = 0
        chairs = 0
        for char in s:
            if char == "E":
                chairs +=1
            else:
                chairs -=1
            if max_chairs<chairs:
                max_chairs = chairs
        return max_chairs
