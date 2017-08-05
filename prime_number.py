'''输出100以内的所有素数，素数之间以一个空格区分（注意，最后一个数字之后不能有空格）。
isPrime函数判断数字n是否为素数，primeIn函数返回一个n以内的素数元组'''
#coding:utf-8

def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2,n):
            if n % i == 0:
                return False
        return True

def primeIn(n):
    return (g for g in range(2,n) if isPrime(g))

print(' '.join(str(x) for x in primeIn(100)))