class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        max_words = 0
        for i in range(len(sentences)):
            temp = len(sentences[i].split(" "))
            if temp > max_words:
                max_words = temp
        return max_words
