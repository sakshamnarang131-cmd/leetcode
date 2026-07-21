class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        n = len(fruits)
        count = len(fruits)
        for i in range(n):
            j=0
            while j< len(baskets):
                if fruits[i] <= baskets[j]:
                    count -= 1
                    baskets.remove(baskets[j])
                    break
                j+=1
        return count
