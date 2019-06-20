#因为行和和列和要相等，所以必须和能被3整除。
#因为之前做过类似的笔试题，所以直接套1到9的9宫格来看是否满足条件。
#   2   9   4
#   7   5   3
#   6   1   8
#不过我也不确定这个二维数组是否满足所有条件，因为我觉得不同数组的权值都有变化，这个模板不一定包含所有情况。

import random
list = [random.randint(1, 99) for j in range(1, 10)]
print(list)
if sum(list)//3>0:
    print('false')
else:
    list = sorted(list)
    list2 = [[list[1],list[8],list[3]],
         [list[6],list[4],list[2]],
         [list[5],list[0],list[7]]]
    a = sum(list2[0])
    b = sum(list2[1])
    c = sum(list2[2])
    d = list2[0][0]+list2[1][0],list2[2][0]
    e = list2[0][1]+list2[1][1],list2[2][1]
    f = list2[0][2]+list2[1][2],list2[2][2]
    g = list2[0][0]+list2[1][1],list2[2][2]
    h = list2[0][2]+list2[1][1],list2[2][0]
    list3 = [a,b,c,d,e,f,g,h]
    set = set(list3)
    if(len(set)>1):
        print('false')
    else:
        print('true')
