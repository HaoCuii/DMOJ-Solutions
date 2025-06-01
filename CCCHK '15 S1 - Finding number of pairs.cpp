#include <bits/stdc++.h>
using namespace std;

const int mod = 1e9 + 7;
using ll = long long;
int n, m;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> m;
    vector<int> nums(n);
    for (int i = 0; i < n; i++)
        cin >> nums[i];

    sort(nums.begin(), nums.end());
    ll cnt = 0;

    for (int i = 0; i < n; i++) {
        int limit = m - nums[i];
        auto it = upper_bound(nums.begin() + i + 1, nums.end(), limit);
        cnt += (it - (nums.begin() + i + 1));
    }

    cout << cnt % mod << "\n";
    return 0;
}
