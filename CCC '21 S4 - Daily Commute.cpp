/*
The optimal combination is subway first then walkway (can be multiple joined)
This is because if i take walkway to skip the subway, i'll still have to wait for the subway to catch back up until i take it again.
To find the continuation it's just start idx, length. (preprocess and keep a list of these)
Whenever query changes two positions just see if the new changes are better than the "best". if so make it the best and do with that
Also whenever you query always do min(best,just use subway)

To proprocess we just do bfs starting from the target, then work backwards storing each node's minimum time.
*/

#include <bits/stdc++.h>
using namespace std;
const int INF = 1000000000;

int main(){
    int n,w,d; cin >> n; cin >> w; cin >> d;
    vector<vector<int>> walks(n);
    for (int i = 0; i < w; i++){
        int a,b; cin >> a >> b; a--; b--;
        walks[b].push_back(a); //for our bfs backwards
    }
    vector<int> station(n);
    vector<int> index(n); //index of each node in station
    for (int i = 0; i < n; i++){
        cin >> station[i]; station[i]--;
        index[station[i]] = i;
    }

    vector<int> paths(n, INF);  
    queue<tuple<int,int>> q;
    unordered_set<int> vis;
    multiset<tuple<int,int>> best;

    q.push({n-1,0});
    paths[n-1] = 0;
    vis.insert(n-1);
    best.insert({index[n-1]+paths[n-1],n-1});

    while (!q.empty()){
        auto [u,l] = q.front();
        q.pop();

        for (int v: walks[u]){
            if (!vis.count(v)){
                q.push({v,l+1});
                vis.insert(v);
                paths[v] = l+1;
                best.insert({l+1+index[v],v});
            }
        }
    }

    for (int i = 0; i < d; i++){
        int x,y; cin >> x >> y; x--; y--;
        int sx = station[x];
        int sy = station[y];

        best.erase({paths[sx] + index[sx], sx});
        best.erase({paths[sy] + index[sy], sy});

        swap(station[x], station[y]);
        index[sx] = y;
        index[sy] = x;

        best.insert({paths[sx] + index[sx], sx});
        best.insert({paths[sy] + index[sy], sy});

        
        auto [a,b] = *best.begin();
        if (a >= INF) cout << index[n-1] << "\n";
        else cout << a << "\n";

    }
    return 0;
}
