class Solution(object):
    def uniqueXorTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique_nums = list(set(nums))
        n = len(unique_nums)
        pairs = set()
        add_pair = pairs.add
        
        for i in xrange(n):
            u_i = unique_nums[i]
            for j in xrange(i, n):
                add_pair(u_i ^ unique_nums[j])
        triplets = set()
        add_triplet = triplets.add
        
        for p in pairs:
            for u in unique_nums:
                add_triplet(p ^ u)
                
        return len(triplets)
