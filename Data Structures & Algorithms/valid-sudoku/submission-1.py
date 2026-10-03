class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sub = dict()
        col = dict()
        row = dict()
        for i in range(9):
            row[i] = set()
            col[i] = set()
            sub[i] = set()

        for i in range(len(board)):
            for j in range (len(board[i])):
                
                val = board[i][j]
                if val == '.':
                    continue

                # row
                if val in row[i]:
                    print("row")
                   
                    return False
                else:
                    row[i].add(val)
                
                # col
                if val in col[j]:
                    print("col")

                    return False
                else:
                    col[j].add(val)
                
                #sub
                id = (i//3)*3 + j//3
                if val in sub[id]:
                    print("sub")
                    print (i)
                    print(j)
                    print(id)

                    print (sub[id])

                    return False
                else:
                    sub[id].add(val)
        
        return True

                

        