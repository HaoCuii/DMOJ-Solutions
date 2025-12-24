#include <bits/stdc++.h>
using namespace std;

int n, dp[10000];
int main(){
    cin >> n;
    vector<vector<int>> paths(n + 1);
    while (true) {
        int a,b; cin >> a >> b;
        if (a == 0){
            break;
        }
        paths[a].push_back(b);
    }
    dp[1] = 1;
    for (int i = 1; i < n; i++){
        for (int b: paths[i]){
            dp[b] += dp[i];
        }
    }
    cout << dp[n];
    return 0;
}