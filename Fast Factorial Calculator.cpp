#include <bits/stdc++.h>
using namespace std;

using ll = long long;
const ll mod = 4294967296;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    ll N; cin >> N;
    for (ll idx = 0; idx < N; idx++){
        ll n; cin >> n;
        ll fact = 1;
        if (n >= 34){
            cout << 0 << "\n";
        }
        else{
            for (ll i = 1; i <= n; i++){
                fact *= i;
            }
            cout << fact % mod << '\n';
        }
    }
}
