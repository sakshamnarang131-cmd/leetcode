class Solution(object):
    def scoreValidator(self, events):
        """
        :type events: List[str]
        :rtype: List[int]
        """
        score = 0
        counter = 0
        i = 0
        while i<len(events) and counter != 10:
            if events[i] == "W":
                counter += 1
            elif events[i] == "WD" or events[i] == "NB":
                score += 1
            else:
                score += int(events[i])
            i+=1
        return [score, counter]
