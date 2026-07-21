class Solution(object):
    def maxActiveSectionsAfterTrade(self, s):
        """
        :type s: str
        :rtype: int
        """
        initial_ones = 0
        zeros = []
        current_zeros = 0
        for char in s:
            if char == '1':
                initial_ones += 1
                if current_zeros > 0:
                    zeros.append(current_zeros)
                    current_zeros = 0
            else:
                current_zeros += 1
        if current_zeros > 0:
            zeros.append(current_zeros)
        if len(zeros) < 2:
            return initial_ones
        max_gain = 0
        for i in range(len(zeros) - 1):
            max_gain = max(max_gain, zeros[i] + zeros[i + 1])
            
        return initial_ones + max_gain
