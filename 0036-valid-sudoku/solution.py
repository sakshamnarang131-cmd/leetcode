class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            s = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] not in s:
                        s.add(board[i][j])
                    else:
                        return False
        for i in range(9):
            s = set()
            for j in range(9):
                if board[j][i] != ".":
                    if board[j][i] not in s:
                        s.add(board[j][i])
                    else:
                        return False
        for box_row in range(3):
            for box_column in range(3):
                s = set()
                for i in range(3):
                    for j in range(3):
                        row = box_row *3 + i
                        column = box_column *3 +j
                        if board[row][column] != ".":
                            if board[row][column] not in s:
                                s.add(board[row][column])
                            else:
                                return False
        return True
