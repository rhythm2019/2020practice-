'''
@说明：骑士漫游，常规深度搜索（用栈实现）。
@author:rhythm
@date:20200321

'''
def next_XY(path: list, cur_x: int, cur_y: int, direc=-1):
    '''
    本程序返回当前位置(cur_x,cur_y)的下一个合理位置
    如果没有下一个合理位置，返回False
    direc:上次访问完的位置
    '''
    direction = [[-2, -1, 1, 2, 2, 1, -1, -2], [1, 2, 2, 1, -1, -2, -2, -1]]
    length = len(direction[0])
    i = direc + 1
    while i < length:
        next_x = cur_x + direction[0][i]
        next_y = cur_y + direction[1][i]
        if 0 <= next_x <= 7 and 0 <= next_y <= 7 and (next_x,
                                                      next_y) not in path:
            return next_x, next_y, i
        else:
            i += 1
    else:
        return False


if __name__ == "__main__":
    path = []
    dire = []
    beginx = 0
    beginy = 0
    path = [(beginx, beginy)]
    dire = [-1]
    i = 1
    while i < 64:
        curx = path[-1][0]
        cury = path[-1][1]
        nextXY = next_XY(path, curx, cury, dire[-1])
        if nextXY:
            path.append((nextXY[0], nextXY[1]))
            dire[-1] = nextXY[2]
            dire.append(-1)
            i += 1
        #回退
        else:
            i -= 1
            path.pop()
            dire.pop()
    print(*path)