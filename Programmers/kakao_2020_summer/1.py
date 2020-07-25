def solution(numbers, hand):
    answer = ""
    posL = "*"
    posR = "#"
    keyPad = {"1": (0, 0), "2": (0, 1), "3": (0, 2), "4": (1, 0), "5": (1, 1), "6": (
        1, 2), "7": (2, 0), "8": (2, 1), "9": (2, 2), "*": (3, 0), "0": (3, 1), "#": (3, 2)}
    for e in numbers:
        cmd = str(e)
        if (cmd in ["1", "4", "7", "*"]):
            answer = answer + "L"
            posL = cmd
        elif (cmd in ["3", "6", "9", "#"]):
            answer = answer + "R"
            posR = cmd
        else:
            curCmd = keyPad[cmd]
            lenFromLeft = abs(curCmd[0] - keyPad[posL][0]) + \
                abs(curCmd[1] - keyPad[posL][1])
            lenFromRight = abs(curCmd[0] - keyPad[posR][0]) + \
                abs(curCmd[1] - keyPad[posR][1])
            if (lenFromLeft == lenFromRight):
                if (hand == "right"):
                    answer = answer + "R"
                    posR = cmd
                else:
                    answer = answer + "L"
                    posL = cmd
            elif (lenFromLeft < lenFromRight):
                answer = answer + "L"
                posL = cmd
            else:
                answer = answer + "R"
                posR = cmd
    return answer


d = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
h = "left"
print(solution(d, h))
