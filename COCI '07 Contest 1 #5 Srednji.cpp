#include <bits/stdc++.h>
using namespace std;
using ll = long long;

//>b = 1 <b = -1 b = 0
//now just find all contiguous arrays that add up to 0, using maps

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, B;
    cin >> n >> B;
    vector<int> A(n+1), psa(n+1);
    int ib = -1;

    for(int i = 1; i <= n; i++){
        cin >> A[i];
        if (A[i] > B) psa[i] = psa[i-1] + 1;
        else if (A[i] < B) psa[i] = psa[i-1] - 1;
        else {psa[i] = psa[i-1]; ib = i;}
    }

    array<unordered_map<int,ll>,2> freq;
    freq[0][0] = 1; 

    for(int j = 1; j < ib; j++){
        freq[j%2][ psa[j] ]++;
    }
    ll ans = 0;
    for(int i = ib; i <= n; i++){
        int want = 1 - (i % 2);
        ans += freq[want][ psa[i]];
        ans += freq[want][psa[i] - 1]; 
    }
    cout << ans << "\n";
    return 0;
}
