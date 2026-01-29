#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
typedef long long ll;
typedef vector<ll> v_i;


int main(){
    int t; cin >> t;

    vector<ll> outputs;
    outputs.reserve(t);

    while (t--){
        int n; cin >> n;
        bool truth = true;
        vector<v_i> plants(n, v_i(3));

        for (int j = 0; j < 3; j++) {
            for (int i = 0; i < n; i++) {
                cin >> plants[i][j];
            }
        }

        sort(plants.begin(), plants.end(), [](const vector<ll>& a, const vector<ll>& b) {
            if (a[1] != b[1])
                return a[1] > b[1];
            return a[0] > b[0];
        });


        for (int i = 0; i < n-1; i++){
            if (i != plants[i][2]) {
                // cout << -1 << "\n";
                truth = false;
                break;
            }
            if (plants[i][0] == plants[i+1][0] && plants[i][1] == plants[i+1][1]){
                // cout << -1 << "\n";
                truth = false;
                break;
            }
        }


        int count = -1;
        while (truth){
            int counter = 0;

            for (int i = 0; i < n-1; i++){
                if (plants[i][0] <= plants[i+1][0]) break;
                else if (plants[i][0] > plants[i+1][0]) counter++;
            }

            if (counter >= n-1) truth = false;

            for (int i = 0; i < n; i++){
               plants[i][0] += plants[i][1];
            }
            count++;
        }

        outputs.push_back(count);

    }

    for (ll x : outputs) cout << x << '\n';
}
