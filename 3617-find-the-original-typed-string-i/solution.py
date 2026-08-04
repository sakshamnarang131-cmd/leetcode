class Solution(object):
    def possibleStringCount(self, word):
        """
        :type word: str
        :rtype: int
        """
        result = 1
        for i in range(1,len(word)):
            if word[i] == word[i-1]:
                result +=1
        return result
