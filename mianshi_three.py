#初步思考是考虑峰值的问题，最大最小值的问题
#假设所有天数的价格构成一个List
#我们需要做的是在两次交易之后获得最大值。
#第一次交易完之后是在list前一部分实现最大利益
#第二次交易完之后是在list后一部分实现最大利益
#最后得到的值为最大即可
#有两种考虑，第一种只考虑最大差值，然后再最大差值之前获利最多，即将峰值最小值之前划为list1,峰值最小值之后划为list2
#第二种考虑为最大差值之间还有一个小峰差，可以卖出买入获利更多。即将峰值最小值到第二大峰值直接划为list1，峰值第二小值到最大峰值划为list2
#动态规划只会做一次交易的，所以将list分为两块，第一次做完动态规划之后传值给第二次得到结果，按两种考虑分别得到结果统计最大值
#这道题借鉴了网上的代码，我自己写的实在是不堪入目，太长了，可能还是想法没理清楚。
#时间复杂度为7*len(list)（假设List无限大）
import random

def solution1(list):
    if not list:
        return 0
    g = [0,0,0]
    l = [0,0,0]
    for i in range(len(list)-1):
        diff = list[i+1] - list[i]
        for j in range(2,0,-1):
            l[j] = max(g[j - 1] + max(diff, 0), l[j] + diff)
            g[j] = max(l[j], g[j])
    return g[2]
if __name__ == '__main__':
    list = [random.randint(1, 99) for j in range(1, 10)]
    print(list)
    max=solution1(list)
    print(max)