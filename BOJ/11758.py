import sys
import math

input = sys.stdin.readline

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

v1 = (x2 - x1, y2 - y1)
v2 = (x3 - x1, y3 - y1)

tmp = math.sqrt(v1[0] ** 2 + v1[1] ** 2) * math.sqrt(v2[0] ** 2 + v2[1] ** 2)

theta = math.asin((v1[0] * v2[1] - v1[1] * v2[0]) / tmp)

if theta == 0: print(0)
if theta > 0: print(1)
if theta < 0: print(-1)
