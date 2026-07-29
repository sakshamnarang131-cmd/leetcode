class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        n = len(words)
        m = len(words[0])
        result = []
        for j in range(m):
            is_present = True
            for i in range(1,n):
                if words[0][j] in words[i]:
                    words[i] = words[i].replace(words[0][j], "", 1)
                else:
                    is_present = False
                    break
            if is_present:
                result.append(words[0][j])
        return result
