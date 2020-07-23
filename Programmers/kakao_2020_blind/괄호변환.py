'''
1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 
   더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
  3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
  4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
  4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
  4-3. ')'를 다시 붙입니다. 
  4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
  4-5. 생성된 문자열을 반환합니다.
  
'''


from collections import defaultdict


def isCorrect(s):
    f = 0
    for e in s:
        if e == '(':
            f += 1
        else:
            f -= 1
            if f < 0:
                return False
    return True


def editU(s):
    s = s[1:-1]
    s = list(s)
    ret = ""
    for c in s:
        if (c == '('):
            ret += ')'
        else:
            ret += '('
    return ret


def solution(s):
    if len(s) == 0:
        return s
    dic = defaultdict(int)
    idx = 0
    for i, e in enumerate(list(s)):
        dic[e] += 1
        if (dic['('] == dic[')']):
            idx = i
            break
    u = s[:idx+1]
    v = s[idx+1:]
    if not isCorrect(u):
        tmp = "("
        tmp += solution(v)
        tmp += ")"
        tmp += editU(u)
        return tmp
    else:
        return u + solution(v)


t = "()))((()"
print(solution(t))


# 다른사람 풀이와 비교
def solution(p):
    if p == '':         # len(s)==0 보다 이게 더 깔끔함
        return p
    r = True
    c = 0
    for i in range(len(p)):
        if p[i] == '(':
            c -= 1
        else:
            c += 1
        if c > 0:      # ')' 가 하나라도 더 생기면 바로 r = False로 만들어서 올바른 괄호 문자열이 아니게 만든다.
            r = False
        if c == 0:     # 균형잡힌 괄호 문자열인 경우에 진입
            if r:      # 올바른 괄호 문자열이면 u를 분리하고 solution(v)를 재귀호출해서 그대로 리턴
                return p[:i+1]+solution(p[i+1:])
            else:      # 올바른 괄호 문자열이 아니라면 문제에서 주어진대로 처리함. 괄호방향 뒤집는것을 map으로 람다함수 만들어서 호출
                return '('+solution(p[i+1:])+')'+''.join(list(map(lambda x: '(' if x == ')' else ')', p[1:i])))
