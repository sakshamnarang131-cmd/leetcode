from collections import Counter
from bisect import bisect_right

class Solution(object):
    def gcdValues(self, nums, queries):
        max_val = max(nums)
        freq = Counter(nums)
        
        multiples_count = [0] * (max_val + 1)
        for i in xrange(1, max_val + 1):
            for j in xrange(i, max_val + 1, i):
                multiples_count[i] += freq[j]
        
        gcd_count = [0] * (max_val + 1)
        for i in xrange(max_val, 0, -1):
            c = multiples_count[i]
            total_pairs = (c * (c - 1)) // 2  
            gcd_count[i] = total_pairs
            
            for j in xrange(2 * i, max_val + 1, i):
                gcd_count[i] -= gcd_count[j]
        
        prefix_sums = [0] * (max_val + 1)
        current_sum = 0
        for i in xrange(1, max_val + 1):
            current_sum += gcd_count[i]
            prefix_sums[i] = current_sum
            
        final = []
        for q in queries:
            gcd_val = bisect_right(prefix_sums, q)
            final.append(gcd_val)
            
        return final
