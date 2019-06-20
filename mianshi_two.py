#仅求这样的0，该0所在行中被两个1包围，该0所在列中被两个1包围;
#先找出这种0，然后全部变为2
#在地图中搜索2，如果有2，找到其周围所有的2。
# 统计个数记为max，然后全部变为1，再次检索2，重复上步操作，如个数超过max，则max更新，直至地图中没有2
#感觉好像做多了，如果是统计行列被1包围的个数，函数fist执行完后统计2的个数即可。
#second执行完后会返回完全被1包围的0，即包围圈内的2周围没有0在附近。
#third执行完后回返回最大岛
#时间复杂度为len(list[])^2（假设list长度无限大）
import random

def first(list):
    for a in range(1,5):
        for b in range(1,5):
            if list[a][b] == 0:
                left = [list[a][x] for x in range(0,b)]
                right = [list[a][x] for x in range(b+1,6)]
                top = [list[x][b] for x in range(0,a)]
                bottom = [list[x][b] for x in range(a+1,6)]
                if 1 in left and 1 in right and 1 in top and 1 in bottom:
                    list[a][b] = 2

def second(list):
    flag=0
    for a in range(1,5):
        for b in range(1,5):
            if list[a][b] == 2:
                left = list[a][b-1]
                right = list[a][b+1]
                top = list[a-1][b]
                bottom = list[a+1][b]
                if left==0 or right==0 or top==0 or bottom==0:
                    list[a][b]=0
                    flag=1
    if(flag):
        second(list)
    else:
        pass

def third(list):
    dao = []
    for i in range(1, 6):
        for j in range(1, 6):
            if list[i][j] == 2:
                # 将每个岛群的面积放在列表中
                dao.append(search(list, i, j))
    return dao


def search(list, i, j):
    if 0 <= i < 6 and 0 <= j < 6 and list[i][j] == 2:
        list[i][j] = 1
        return 1 + search(list,i-1,j)+ search(list,i+1,j)+ search(list,i,j-1)+ search(list,i,j+1)
    else:
        return 0

if __name__ == '__main__':

    list = [[1, 1, 1, 1, 1, 1]]
    for i in range(1, 5):
        list.append([random.randint(0, 1) for j in range(1, 7)])
    list.append([1, 1, 1, 1, 1, 1])
    for s in range(1, 7):
        print(list[s - 1])
    first(list)
    print('\n')
    for s in range(1, 7):
        print(list[s - 1])
    second(list)
    print('\n')
    for s in range(1, 7):
        print(list[s - 1])
    list_dao = third(list)
    if(list_dao==[]):
        print(1)
    else:
        print(max(list_dao))