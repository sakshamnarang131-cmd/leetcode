class Solution(object):
    def rowAndMaximumOnes(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        max_count =0
        temp = 0
        for i in range(len(mat)):
            count = 0
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    count += 1
            if count > max_count:
                temp = i
                max_count = count
        return [temp,max_count]
