class Solution(object):
    def numberOfLines(self, widths, s):
        """
        :type widths: List[int]
        :type s: str
        :rtype: List[int]
        """
        pixels = 0
        i=0
        lines = 1
        while i < len(s):
            pixels += widths[ord(s[i]) - 97]
            if pixels > 100:
                pixels = 0
                i -= 1
                lines += 1
            i+=1
        return [lines, pixels]
