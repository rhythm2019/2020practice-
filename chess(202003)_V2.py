'''
@说明：骑士漫游，常规深度搜索（用栈实现），状态转移采用优化算法（贪婪函数或者先验）。
@author:rhythm
@date:20200321

'''
def next_XY(path: list, visit: list):
    '''
    本程序返回当前位置(cur_x,cur_y)的下一个合理位置
    如果没有下一个合理位置，返回False
    cur_x:当前节点坐标
    cur_y:当前节点坐标
    direc:当前节点上次访问完的位置
    '''
    global MOVE, WEIGHT
    cur_x = path[-1][0]
    cur_y = path[-1][1]
    dire = path[-1][2]
    #下一个行棋方向选择
    i = dire + 1
    while i < len(WEIGHT[cur_x][cur_y]):
        next_pos = WEIGHT[cur_x][cur_y][i]
        next_x, next_y = MOVE[cur_x][cur_y][next_pos]
        if visit[next_x][next_y] == 0:
            return next_x, next_y, i
        else:
            i += 1
    else:
        return False


def set_WEIGHT(cur_x, cur_y, visit: list):
    '''
    本程序计算当前节点(cur_x,cur_y)的每一个下一步位置，计算每个下一步位置的出度（考虑位置），并且排序
    move_sort:nx,ny的出度计算
    '''
    global MOVE, WEIGHT
    move_sort = []
    for i in range(len(MOVE[cur_x][cur_y])):
        #nx,ny为下一步位置
        nx, ny = MOVE[cur_x][cur_y][i]
        if visit[nx][ny] == 0:
            count = 0
            #计算出度
            #nnx,nny为nx,ny的下一步位置
            for next_pos in MOVE[nx][ny]:
                nnx, nny = next_pos
                if visit[nnx][nny] == 0:
                    count += 1
            move_sort.append(count)
        else:
            move_sort.append(9)
    sorted_index = [
        idx for idx, v in sorted(enumerate(move_sort), key=lambda x: x[1])
    ]
    WEIGHT[cur_x][cur_y] = sorted_index
    return


def set_MOVE():
    '''
    本程序返回棋盘(X,Y)坐标下的所有下一步行棋坐标选择,排除超出边界情况，没有考虑下一个位置是否遍历  
    '''
    direction = [[-2, -1, 1, 2, 2, 1, -1, -2], [1, 2, 2, 1, -1, -2, -2, -1]]
    MOVE = [[[] for i in range(8)] for j in range(8)]
    x = 0
    while x < 8:
        y = 0
        while y < 8:
            for i in range(len(direction[0])):
                next_x = x + direction[0][i]
                next_y = y + direction[1][i]
                if 0 <= next_x <= 7 and 0 <= next_y <= 7:
                    MOVE[x][y].append((next_x, next_y))
            y += 1
        x += 1
    return MOVE


if __name__ == "__main__":
    '''
    path:[(x,y,dire)]棋子走过的路径；
    dire:path中每步棋的当前的方向(带权重排序后)；
    visit:节点状态列表，0未搜索过，1已搜索过；
    MOVE[8][8],XY走标下的方向选择；
    WEIGHT,path路径下MOVE的权重调整,如节点已经搜索过，设置为9
    '''
    beginx = 0
    beginy = 0
    dire = -1
    #节点状态矩阵
    visit = [[0 for i in range(8)] for j in range(8)]
    visit[beginx][beginy] = 1
    path = [[beginx, beginy, dire]]
    MOVE = set_MOVE()
    WEIGHT = [[0 for i in range(8)] for j in range(8)]
    set_WEIGHT(beginx, beginy, visit)
    i = 1
    while 0 < i < 64:
        nextXY = next_XY(path, visit)
        if nextXY:
            path[-1][2] = nextXY[2]
            path.append([nextXY[0], nextXY[1], -1])
            visit[nextXY[0]][nextXY[1]] = 1
            set_WEIGHT(nextXY[0], nextXY[1], visit)
            i += 1
        #回退
        else:
            visit[path[-1][0]][path[-1][1]] = 0
            WEIGHT[path[-1][0]][path[-1][1]] = 0
            path.pop()
            i -= 1
    print(*path)