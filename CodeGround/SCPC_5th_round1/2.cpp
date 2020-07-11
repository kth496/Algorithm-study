#include <bits/stdc++.h>
#define _USE_MATH_DEFINES  // M_PI를 사용
#include <math.h>
#define Bi blocks[i]
#define PI 3.141692

using namespace std;

double Answer;
int blocks[1002][3];
int T, test_case, R, S, E, N;

double climbing(int st, int end) {
    double ret = (double)(end - st);
    for (int i = 0; i < N; i++) {
        if (Bi[2] < R) {
            // 이 부분에서 double로 형변환 안해주면
            // 2/5 같은 상황에서도 cos가 0으로 잡힌다.
            double cos = ((double)R - (double)Bi[2]) / (double)R;
            double theta = acos(cos);
            double tmp = (double)(2 * R * (theta - sin(theta)));
            ret += tmp;
        } else {
            ret += (double)(M_PI * R);
            ret += (double)(2 * (Bi[2] - R));
            ret -= (double)(2 * R);
        }
    }
    return ret;
}

int main(int argc, char** argv) {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    // fixed 를 안하면 precision이 정수부를 포함한 자리수로 출력됨
    cout << fixed;
    cout.precision(7);
    cin >> T;
    for (test_case = 0; test_case < T; test_case++) {
        cin >> R >> S >> E;  // 반지름, 출발, 도착좌표
        cin >> N;
        for (int i = 0; i < N; i++) cin >> Bi[0] >> Bi[1] >> Bi[2];  // li ri hi
        Answer = climbing(S, E);
        cout << "Case #" << test_case + 1 << endl;
        cout << Answer << endl;
    }

    return 0;  // Your program should return 0 on normal termination.
}