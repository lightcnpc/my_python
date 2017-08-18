'''给你一个整数列表L, 输出L的中位数（若结果为小数，则保留一位小数）。

例如： L=[0,1,2,3,4]

则输出：2'''

#coding:utf-8

def creatList(n):
    return list(range(n))

def get_median(n):
    L = list(range(n))
    if n%2 !=0:
        return L[n//2]
    else:
        return (L[n//2-1]+L[n//2])/2

print(get_median(5))