from collections import defaultdict

def isRightEdge(point):
    return point[0] == 8
def isBottomEdge(point):
    return point[1] == 8

def getRowKey(point):
    return ('row', point[1])

def getColKey(point):
    return ('col', point[0])

def getBoxKey(point):
    x = point[0] // 3
    y = point[1] // 3
    return (x, y)

def getValue(point, board: List[List[str]]):
    return board[point[1]][point[0]]

class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        map = defaultdict(set)

        q = deque()
        visited = set()

        q.append((0,0))
        
        while len(q) != 0:

            p = q.pop()

            if p in visited:
                continue
            
            visited.add(p)

            if not isRightEdge(p):
                q.append((p[0]+1, p[1]))
            
            if not isBottomEdge(p):
                q.append((p[0], p[1] + 1))

            val = getValue(p, board)

            if val == '.':
                continue

            # Handle Row
            rowKey = getRowKey(p)
            rowSet = map[rowKey]
            if val in rowSet:
                return False
            else:
                rowSet.add(val)
            
            # Handle Column
            colKey = getColKey(p)
            colSet = map[colKey]
            if val in colSet:
                return False
            else:
                colSet.add(val)

            # Handle Box
            boxKey = getBoxKey(p)
            boxSet = map[boxKey]
            if val in boxSet:
                return False
            else:
                boxSet.add(val)

        return True

            



