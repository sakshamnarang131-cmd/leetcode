class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        title = title.lower()
        words = title.split()
        for i in range(len(words)):
            if len(words[i]) > 2:
                words[i] = words[i].capitalize()
        return " ".join(words)
