'''给你一个整数组成的列表L，按照下列条件输出：
若L是升序排列的,则输出"UP";
若L是降序排列的,则输出"DOWN";
若L无序，则输出"WRONG"。'''

#coding:utf-8

def isListSorted(L):
    '''使用sorted（）函数，是因为要保留原始L，L.sort（）会改变L，不应在此使用'''
    if sorted(L) == L:
        print('UP')
    elif sorted(L,reverse = True) == L:
        print('DOWN')
    else:
        print('WRONG')

isListSorted(L)