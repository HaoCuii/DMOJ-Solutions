#include <bits/stdc++.h>
using namespace std;

//dp[r][c] - greatest amount of money ending on r,c. 
//recurrence - max from top pass, bottom pass, or left straight to right

static constexpr int NEG_INF = INT_MIN;

inline int cellValue(char ch) {
    if (ch == '*') return NEG_INF;
    if (ch == '.') return 0;
    return ch - '0';
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    while (true) {
        int m, n;
        cin >> m >> n;
        if (!cin || (m == 0 && n == 0))
            break;

        vector<string> grid(m);
        for (int r = 0; r < m; r++) {
            cin >> grid[r];
        }
        vector<vector<int>> dp(m, vector<int>(n, NEG_INF));

        dp[m-1][0] = cellValue(grid[m-1][0]);
        for (int r = m-2; r >= 0; --r) {
            int v = cellValue(grid[r][0]);
            if (v > NEG_INF && dp[r+1][0] > NEG_INF)
                dp[r][0] = dp[r+1][0] + v;
        }

        for (int c = 1; c < n; ++c) {
            vector<int> down(m, NEG_INF), up(m, NEG_INF);

            //left-right
            for (int r = 0; r < m; ++r) {
                int v = cellValue(grid[r][c]);
                if (v > NEG_INF && dp[r][c-1] > NEG_INF) {
                    down[r] = up[r] = dp[r][c-1] + v;
                }
            }

            //top-bottom
            for (int r = 1; r < m; ++r) {
                int v = cellValue(grid[r][c]);
                if (down[r-1] > NEG_INF && v > NEG_INF) {
                    down[r] = max(down[r], down[r-1] + v);
                }
            }

            //bottom-top
            for (int r = m-2; r >= 0; --r) {
                int v = cellValue(grid[r][c]);
                if (up[r+1] > NEG_INF && v > NEG_INF) {
                    up[r] = max(up[r], up[r+1] + v);
                }
            }

            for (int r = 0; r < m; ++r) {
                dp[r][c] = max(down[r], up[r]);
            }
        }

        int answer = dp[m-1][n-1];
        cout << answer << "\n";
    }

    return 0;
}
