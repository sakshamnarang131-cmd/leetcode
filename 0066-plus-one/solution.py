class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(0, len(digits)):
            digits[i] = str(digits[i])
        a = "".join(digits)
        a = int(a)
        a += 1
        a = str(a)
        b = []
        for i in range(0, len(a)):
            b.append(int(a[i]))
        return b
