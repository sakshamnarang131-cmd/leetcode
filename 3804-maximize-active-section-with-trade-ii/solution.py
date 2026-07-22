class SparseTable:
    def __init__(self, arr):
        if not arr: 
            return
        self.n = len(arr)
        self.log = [0] * (self.n + 1)
        for i in range(2, self.n + 1):
            self.log[i] = self.log[i // 2] + 1
        
        self.st = [[0] * (self.log[self.n] + 1) for _ in range(self.n)]
        for i in range(self.n):
            self.st[i][0] = arr[i]
        
        j = 1
        while (1 << j) <= self.n:
            i = 0
            while i + (1 << j) <= self.n:
                self.st[i][j] = max(self.st[i][j - 1], self.st[i + (1 << (j - 1))][j - 1])
                i += 1
            j += 1

    def query(self, L, R):
        if L > R: 
            return 0
        j = self.log[R - L + 1]
        return max(self.st[L][j], self.st[R - (1 << j) + 1][j])


class Solution:
    def _bisect_left(self, a, x):
        lo, hi = 0, len(a)
        while lo < hi:
            mid = (lo + hi) // 2
            if a[mid] < x:
                lo = mid + 1
            else:
                hi = mid
        return lo
        
    def _bisect_right(self, a, x):
        lo, hi = 0, len(a)
        while lo < hi:
            mid = (lo + hi) // 2
            if x < a[mid]:
                hi = mid
            else:
                lo = mid + 1
        return lo

    def maxActiveSectionsAfterTrade(self, s, queries):
        n = len(s)
        total_ones = s.count('1')
        blocks = []
        i = 0
        while i < n:
            if s[i] == '0':
                j = i
                while j < n and s[j] == '0':
                    j += 1
                blocks.append((i, j - 1, j - i)) 
                i = j
            else:
                i += 1
        if not blocks:
            return [total_ones] * len(queries)
            
        starts = [b[0] for b in blocks]
        ends = [b[1] for b in blocks]
        lens = [b[2] for b in blocks]
        m = len(blocks)
        adj = [0] * (m - 1)
        for i in range(m - 1):
            adj[i] = lens[i] + lens[i+1]
        st = SparseTable(adj) if m > 1 else None
        
        ans = []
        for query in queries:
            l, r = query[0], query[1]
            s_idx = self._bisect_left(ends, l)
            e_idx = self._bisect_right(starts, r) - 1
            
            if s_idx > e_idx:
                ans.append(total_ones)
            elif s_idx == e_idx:
                ans.append(total_ones)
            else:
                k = e_idx - s_idx + 1
                Z_0 = min(ends[s_idx], r) - max(starts[s_idx], l) + 1
                Z_last = min(ends[e_idx], r) - max(starts[e_idx], l) + 1
                
                if k == 2:
                    gain = Z_0 + Z_last
                else:
                    gain = max(Z_0 + lens[s_idx + 1], lens[e_idx - 1] + Z_last)
                    
                    if k > 3:
                        max_mid = st.query(s_idx + 1, e_idx - 2)
                        gain = max(gain, max_mid)
                        
                ans.append(total_ones + gain)
                
        return ans
