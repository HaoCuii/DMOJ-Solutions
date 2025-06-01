#include <bits/stdc++.h>
using namespace std;
using ll = long long;
deque<int> gram;
vector<bool> used; 

int main(){
    int n; cin >> n;
    ll x; cin >> x;

    ll capa = 1LL * (n-1) * (n-2) / 2;
    gram.push_front(0);
    if (x > capa){
        cout << -1; return 0;
    }

    for (int i = n-2; i >= 1; i--){
        if (capa - i <= x){
            break;
        }
        gram.push_front(n-i-1);
        capa -= i;
    }

    int want = capa - x;
    gram.push_front(n-1-want);
    used.assign(n + 1, false);
    used[n] = true;
    gram.pop_back();

    for (int i : gram) {
        used[i] = true;
    }
    cout << n << ' ';
    for (int i = 1; i < n; i++){
        if (used[i]) continue;
        cout << i << ' ';
    }
    for (int i : gram){
        cout << i << ' ';
    }
    return 0;
}
