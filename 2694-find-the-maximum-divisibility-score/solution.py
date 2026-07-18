class Solution(object):
    def maxDivScore(self, nums, divisors):
        """
        :type nums: List[int]
        :type divisors: List[int]
        :rtype: int
        """
        score = []
        count = 0
        for i in range(len(divisors)):
            for j in range(len(nums)):
                if nums[j] % divisors[i] == 0:
                    count += 1
            score.append(count)
            count = 0
        max_score = max(score)
        min_value = max(divisors)
        for i in range(len(divisors)):
            if score[i] == max_score:
                if min_value > divisors[i]:
                    min_value = divisors[i]
        return min_value
