#include <bits/stdc++.h>
using namespace std;


//compute the minimum for each i,j basically the rectangle before it
//compute the maximum for each i,j basically the rectangle plus the rows filled
//update the difference array

int diff[25000001];
int n,m,q;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cin >> n >> m >> q;
    for (int i = 1; i <= n; i++){
        for (int j = 1; j <= m; j++){
            int mini = i*j;
            int maxi = (i-1)*(j-1) + (n-i+1)*(j-1) + (m-j+1)*(i-1) + 1;
            diff[mini] ++;
            diff[maxi+1] --;
        }
    }
    for (int i = 1; i <= n*m; i++){
        diff[i] += diff[i-1];
    }
    for (int i = 0; i < q; i++){
        int qi; cin >> qi;
        cout << diff[qi] << '\n';
    }
    return 0;
}