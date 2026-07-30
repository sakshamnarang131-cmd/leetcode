class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        result = 0
        for i in range(len(words1)):
            if words1.count(words1[i]) == 1 and words2.count(words1[i]) == 1:
                result +=1
        return result

