class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        n = len(timePoints)
        min_time = 1440
        for i in range(n):
            timePoints[i] = int(timePoints[i][0] + timePoints[i][1])*60 + int(timePoints[i][3] + timePoints[i][4])
        timePoints.sort()
        for i in range(1,n):
            if (timePoints[i] - timePoints[i-1]) < min_time:
                min_time = timePoints[i] - timePoints[i-1]
        if (1440 - timePoints[-1] + timePoints[0]) < min_time:
            min_time = 1440 - timePoints[-1] + timePoints[0]
        return min_time
