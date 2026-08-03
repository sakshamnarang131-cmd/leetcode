class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        """
        :type moves: str
        :rtype: int
        """
        x = 0
        count = 0
        for char in moves:
            if char == "L":
                x-=1
            elif char == "R":
                x+=1
            else:
                count +=1
        if x>=0:
            return count + x
        else:
            return count - x

