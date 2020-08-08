T = int(input())
for _ in range(T):
    N = int(input())
    out = [0 for _ in range(N)]
    cand = []

    for _ in range(N):
        cand.append(tuple(map(int, input().split())))

    cand = sorted(cand)

    '''
    가장 단순하게 O(N^2)으로 탈락 여부를 확인할 수 있다.
    하지만 입력의 크기가 크기 때문에 이 방법으로는 TLE를 피할 수 없다.
    Tuple을 정렬해두면 O(N)으로 해결할 수 있다.
    '''

    # isFind = False
    # for i in range(N-1):
    #     per1 = cand[i]
    #     if out[i] == 1:  # 이미 탈락
    #         continue

    #     for j in range(i+1, N):
    #         per2 = cand[j]
    #         if out[j] == 1:
    #             continue

    #         # per2 탈락
    #         if per1[0] < per2[0] and per1[1] < per2[1]:
    #             out[j] = 1
    #             print("탈락 : ", per2, " | 원인 : ", per1)
    #         # per1 탈락
    #         elif per1[0] > per2[0] and per1[1] > per2[1]:
    #             out[i] = 1
    #             print("탈락 : ", per1, " | 원인 : ", per2)
    #             break

    # print(cand)
    ans = 0

    bound = cand[0][1]
    for i in range(1, N):
        if cand[i][1] < bound:
            bound = cand[i][1]
            ans += 1

    print(ans+1)
    # print(cand)
    # for i in range(N):
    #     print(cand[i], out[i])
    # print(N - out.count(1))
