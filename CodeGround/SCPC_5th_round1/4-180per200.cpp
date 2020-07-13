#include <bits/stdc++.h>
using namespace std;

int Answer, T, test_case, N, tmp;

int compare(const void* a, const void* b) { return (*(int*)a - *(int*)b); }

map<int, double> solve(vector<int> x, map<int, double> mapp) {
    for (int i = N - 1; i > -1; i--) {
        int R2 = x[i];
        if (i == N - 1)
            mapp[R2] = 0.0;
        else {
            int R1 = x[i + 1];
            double R1d = (double)R1;
            double R2d = (double)R2;
            double theta = acos((R1d - R2d) / (R1d + R2d));
            double h = (R1d - R2d) * tan(theta);
            mapp[R2] = mapp[R1] + h;
        }
    }
    return mapp;
}

int main(int argc, char** argv) {
    cin >> T;
    for (test_case = 0; test_case < T; test_case++) {
        cin >> N;
        vector<int> radius(N), submit(N);
        map<int, double> mapp;
        for (int i = 0; i < N; i++) {
            cin >> tmp;
            radius[i] = tmp;
            submit[i] = tmp;
            mapp.insert(make_pair(i, 0));
        }
        qsort(&radius[0], N, sizeof(int), compare);

        mapp = solve(radius, mapp);

        cout << fixed;
        cout.precision(10);
        cout << "Case #" << test_case + 1 << endl;
        for (int e : submit) cout << mapp[e] << '\n';
    }

    return 0;  // Your program should return 0 on normal termination.
}
