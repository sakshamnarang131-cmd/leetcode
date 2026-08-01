class Solution(object):
    def countPrefixes(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: int
        """
        result = 0
        for i in range(len(words)):
            if len(words[i]) <= len(s):
                is_prefix = True
                for j in range(len(words[i])):
                    if words[i][j] != s[j]:
                        is_prefix = False
                if is_prefix:
                    result += 1
        return result
