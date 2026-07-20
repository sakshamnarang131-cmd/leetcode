class Solution(object):
    def maxDistance(self, moves):
        """
        :type moves: str
        :rtype: int
        """
        final_i = 0
        final_j = 0
        count_U = 0
        count_D = 0
        count_L = 0
        count_R = 0
        moves = list(moves)
        for i in range(len(moves)):
            if moves[i] == 'U':
                count_U +=1
            elif moves[i] == 'D':
                count_D +=1
            elif moves[i] == 'L':
                count_L +=1
            elif moves[i] == 'R':
                count_R +=1
        max_moves = max(count_U, count_D, count_L, count_R)
        for i in range(len(moves)):
            if moves[i] == 'U':
                final_j += 1
            elif moves[i] == 'D':
                final_j -= 1
            elif moves[i] == 'L':
                final_i -= 1
            elif moves[i] == 'R':
                final_i += 1
            elif moves[i] == '_':
                if max_moves == count_U:
                    final_j +=1
                elif max_moves == count_D:
                    final_j -=1
                elif max_moves == count_L:
                    final_i -=1
                elif max_moves == count_R:
                    final_i +=1
        return abs(final_i) + abs(final_j)
