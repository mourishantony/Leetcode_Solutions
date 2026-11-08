class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        i = 0
        while i<9:
            store1 =set()
            store2 = set()
            for j in range(9):
                if board[i][j] == ".":
                    None
                elif board[i][j] in store1:
                    return False
                else:
                    store1.add(board[i][j])


                if board[j][i] == ".":
                    None
                elif board[j][i] in store2:
                    return False
                else:
                    store2.add(board[j][i])
            store3 = set()
            for j in range((i // 3) * 3, (i // 3) * 3 + 3):
                for k in range((i % 3) * 3, (i % 3) * 3 + 3):
                    if board[j][k] == ".":
                        None
                    elif board[j][k] in store3:
                        return False
                    else:
                        store3.add(board[j][k])
            i+=1

        return True