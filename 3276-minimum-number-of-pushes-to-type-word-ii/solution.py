class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        word_freq = {}
        for i in word:
            word_freq[i] = word_freq.get(i, 0) + 1
        freq_sorted = sorted(word_freq.values(), reverse = True)
        result = 0
        for i in range(len(freq_sorted)):
            count = freq_sorted[i]
            multiplier  = (i//8)+1
            result += count*multiplier
        return result
