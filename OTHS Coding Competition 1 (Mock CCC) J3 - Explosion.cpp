#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, d;
    cin >> n >> d;
    int prev; 
    cin >> prev;

    int cnt = 1;
    int longest = 1;
    int curlong = 1;

    for (int i = 1; i < n; i++){
        int cur; 
        cin >> cur;
        if (abs(cur - prev) <= d) {
            curlong++;
        } else {
            longest = max(longest, curlong);
            cnt++;
            curlong = 1;
        }
        prev = cur;
    }

    longest = max(longest, curlong);

    cout << cnt << "\n";
    cout << longest  << "\n";
    return 0;
}
