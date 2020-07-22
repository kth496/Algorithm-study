def solution(brown, yellow):
    h, w = 3, (brown - 2)//2
    while(1):
        if (h*w - (2*h+2*w-4) == yellow):
            return [w, h]
        h += 1
        w -= 1


print(solution(24, 24))
