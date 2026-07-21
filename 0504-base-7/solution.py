import numpy
class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        return numpy.base_repr(num, 7)
