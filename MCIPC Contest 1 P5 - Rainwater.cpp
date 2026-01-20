#include <bits/stdc++.h>
using namespace std;

bool vis[1005][1005];
char grid[1005][1005];

int main() {
    int r, c; cin >> r >> c;

    for (int i = 0; i < r; i++)
        for (int j = 0; j < c; j++)
            cin >> grid[i][j];

    int ans = 0;
    queue<pair<int,int>> q;

    //fill water
    for (int j = 0; j < c; j++) {
        if (grid[0][j] == '.') {
            q.push({0, j});
            vis[0][j] = true;
            grid[0][j] = 'W';
            ans++;
        }
    }

    vector<pair<int,int>> d_fill = {{0,1},{0,-1},{1,0}};

    while (!q.empty()) {
        auto [r1, c1] = q.front();
        q.pop();

        for (auto [dr, dc] : d_fill) {
            int nr = r1 + dr, nc = c1 + dc;
            if (0 <= nr && nr < r && 0 <= nc && nc < c &&
                !vis[nr][nc] && grid[nr][nc] != 'X') {
                q.push({nr, nc});
                vis[nr][nc] = true;
                grid[nr][nc] = 'W';
                ans++;
            }
        }
    }

    //remove drained water
    memset(vis, 0, sizeof(vis));

    // bottom row
    for (int j = 0; j < c; j++) {
        if (grid[r-1][j] == 'W') {
            q.push({r-1, j});
            vis[r-1][j] = true;
            grid[r-1][j] = '.';
            ans--;
        }
    }
    // left + right columns
    for (int i = 0; i < r; i++) {
        if (grid[i][0] == 'W') {
            q.push({i, 0});
            vis[i][0] = true;
            grid[i][0] = '.';
            ans--;
        }
        if (grid[i][c-1] == 'W') {
            q.push({i, c-1});
            vis[i][c-1] = true;
            grid[i][c-1] = '.';
            ans--;
        }
    }

    vector<pair<int,int>> d_drain = {{0,1},{0,-1},{-1,0}}; 

    while (!q.empty()) {
        auto [r1, c1] = q.front();
        q.pop();

        for (auto [dr, dc] : d_drain) {
            int nr = r1 + dr, nc = c1 + dc;
            if (0 <= nr && nr < r && 0 <= nc && nc < c &&
                !vis[nr][nc] && grid[nr][nc] == 'W') {
                q.push({nr, nc});
                vis[nr][nc] = true;
                grid[nr][nc] = '.';
                ans--;
            }
        }
    }

    cout << ans;
    return 0;
}
