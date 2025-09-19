# 코딩테스트를 하루정도 투자해서 Class 1 문제를 모두 풀었다.
# Class 2 문제를 1주일 정도 계속 해볼 것이다.

import sys
input = sys.stdin.readline

temp = int(input())

for i in range(temp):
    H, W, N = list(map(int, input().split()))

    a= N % H
    if a ==0:
        a = H

    b = (N - 1) // H + 1
    print (a * 100  + b)
