import re

expression = input()
ex = re.split(r'(\D)', expression)
# print(ex)

ans = 0
minus = False
for e in ex:
    if e == '-':
        minus = True
    if e != '+' and e != '-':  # 숫자일 경우
        if minus:
            ans -= int(e)
        else:
            ans += int(e)
print(ans)
