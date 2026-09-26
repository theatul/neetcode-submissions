class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = dict()
        col = dict()
        sub = defaultdict(set)
        for i in range(9):
            row[i] = set()
            col[i] = set()
            #sub[i] = set()

        
        for i in range(9):
            for j in range(9):
                tmp  = board[i][j]
                if tmp ==".":
                    continue
                # check row
                if tmp in row[i]:
                    return False
                else:
                    row[i].add(tmp)


                # check col
                if tmp in col[j]:
                    print ("col failed")
                    return False
                else:
                    col[j].add(tmp)

                # check sub-set
                #subset_id = (row // 3, col // 3) #math.ceil(float((i+1) * (j+1)) / float(9)) - 1
                if tmp in sub[(i // 3, j // 3)]:
                    #print ("sub failed")
                    #print(subset_id)
                    #print(tmp)
                    #print ("row failed")
                    #print(sub[(i // 3, j // 3)])
                    return False
                else:
                    sub[(i // 3, j // 3)].add(tmp)

        
        return True
        

        