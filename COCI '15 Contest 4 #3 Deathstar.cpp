#include <bits/stdc++.h>
using namespace std;

int nums[1000];

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; cin >> n;

    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            int val; cin >> val;
            for (int idx = 0; idx < (int)log2(val) + 1; idx++){
                int bit = (val >> idx) & 1;
                if (bit == 1){
                    nums[i] |= 1 << idx;
                    nums[j] |= 1 << idx;
                }
            }
        }
    }
    
    for (int i = 0; i < n; i++){
        cout << nums[i] << ' ';
    }

    return 0;
}