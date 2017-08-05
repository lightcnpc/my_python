'''已知矩形长a,宽b,输出其面积和周长，面积和周长以一个空格隔开。例如：a = 3, b = 8,则输出：24 22'''
#coding:utf-8

def rectangle_area(a,b):
    return a*b

def rectangle_perimeter(a,b):
    return (int(a)+int(b))*2

print(rectangle_area(a,b),' ',rectangle_perimeter(a,b))