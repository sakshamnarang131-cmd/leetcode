class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        spaces = 0
        for i in range(len(sentence)):
            if i ==0 or sentence[i] == " ":
                spaces +=1
                is_prefix = True
                for j in range(len(searchWord)):
                    if i == 0:
                        c = 0
                    else:
                        c = 1
                    if i + j + c >= len(sentence) or searchWord[j] != sentence[i+j+c]:
                        is_prefix = False
                        break
                if is_prefix:
                    return spaces
        return -1
