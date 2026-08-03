class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        n_sum = 0
        n_product = 1
        while n != 0:
            n_sum += n%10
            n_product *= n%10
            n = n//10
        return n_product - n_sum
