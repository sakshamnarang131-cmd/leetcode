class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        n = len(word)
        i=1
        result = 0
        while n>8:
            result += 8*i
            n-=8
            i+=1
        return result+n*i
