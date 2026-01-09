#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    int ans = 0;

    for (int i = 0; i < n; i++) {
        for (int j = 1; j <= n; j++) {
            if (i + j > n) {
                break;
            }

            float avg = 0;
            for (int k = i; k < i + j; k++) {
                avg += arr[k];
            }
            avg /= j;

            for (int k = i; k < i + j; k++) {
                if (arr[k] == avg) {
                    ans++;
                    break;
                }
            }
        }
    }

    cout << ans;
    return 0;
}
