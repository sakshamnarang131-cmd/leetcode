class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        b = [str(x) for x in b]
        return pow(a, int("".join(b)), 1337)
