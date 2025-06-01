#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int n, s, t;
ll psa[1000001];

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> s >> t;
    for(int i = 1; i <= n; i++){
        ll x; 
        cin >> x;
        psa[i] = psa[i-1] + x;
    }

    int blocks = (n + s - 1) / s;
    ll ans = 0;

    for(int i = 0; i <= t; i++){
        int leftcnt  = min(n, i * s);
        int rightcnt = min(n, (t - i) * s);   
        ll l = psa[leftcnt];
        ll r = psa[n] - psa[max(leftcnt,max(0, n - rightcnt))];
        ans = max(ans, l + r);
    }

    cout << ans << "\n";
    return 0;
}
