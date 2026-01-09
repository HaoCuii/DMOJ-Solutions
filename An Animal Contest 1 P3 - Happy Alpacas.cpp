#include <bits/stdc++.h>
using namespace std;

int main(){
    int n,x; cin >> n >> x;
    if (n%2 != x%2){
        cout << -1 << '\n';
        return 0;
    }
    
    vector<int> h;
    for (int i = 0; i < n; i++){
        h.push_back(0);
    }

    for (int i = 0; i < (n-x)/2; i++){
        h[i*2] = 1;
    }

    for (int i = 0; i < h.size(); i++) {
        cout << h[i];
        if (i + 1 < h.size()) cout << " ";
    }
    cout << '\n';

    return 0;
}