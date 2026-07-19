class Solution(object):
    def maximumValue(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        result = 0
        for i in range(len(strs)):
            temp = 0
            for j in range(len(strs[i])):
                if ord(strs[i][j]) < 48 or ord(strs[i][j]) > 57:
                    temp = len(strs[i])
                    break
            if temp == 0:
                temp = int(strs[i])
            result = max(temp, result)
        return result
