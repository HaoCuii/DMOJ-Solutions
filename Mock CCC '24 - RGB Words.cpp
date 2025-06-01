#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n; cin >> n;
    string rgb; cin >> rgb;
    ll ans = 0;
    ll good = 0; ll bad = 0;
    for (char i: rgb){
        if (i == 'R'){
            bad ++;
        }
        if (i == 'G'){
            good = 0;
            good += bad;
            bad = 0;
        }
        if (i == 'B'){
            ans += good;
        }
    }
    cout << ans;
    return 0;
}