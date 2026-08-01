class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        result = 0
        for i in range(len(words)):
            if len(words[i]) < len(pref):
                continue
            is_prefix = True
            for j in range(len(pref)):
                if pref[j] != words[i][j]:
                    is_prefix = False
                    break
            if is_prefix:
                result += 1
        return result
