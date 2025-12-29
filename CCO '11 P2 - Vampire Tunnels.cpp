#include <iostream>
#include <vector>
#include <queue>
#include <limits>
#include <algorithm>

using namespace std;

struct Edge {
    int to;
    int time;
    int hullCost;
};

struct State {
    int time;
    int hull;
    int island;
    bool operator>(const State &other) const {
        return time > other.time;
    }
};

int main() {
    int hull;
    cin >> hull;
    
    int num_islands, sea_routes;
    cin >> num_islands >> sea_routes;

    vector<vector<int>> dist(num_islands, vector<int>(hull + 1, numeric_limits<int>::max()));

    vector<vector<Edge>> graph(num_islands);

    for (int i = 0; i < sea_routes; ++i) {
        int isl1, isl2, time, hull_cost;
        cin >> isl1 >> isl2 >> time >> hull_cost;
        graph[isl1].push_back({isl2, time, hull_cost * time});
        graph[isl2].push_back({isl1, time, hull_cost * time});
    }

    int start = 0, end = num_islands - 1;
    priority_queue<State, vector<State>, greater<State>> queue;
    queue.push({0, 0, start});
    dist[start][0] = 0;

    while (!queue.empty()) {
        State current = queue.top();
        queue.pop();

        int t = current.time;
        int h = current.hull;
        int isl = current.island;

        for (const auto &edge : graph[isl]) {
            int nh = edge.hullCost + h;
            int nt = edge.time + t;
            if (nh <= hull && nt < dist[edge.to][nh]) {
                dist[edge.to][nh] = nt;
                queue.push({nt, nh, edge.to});
            }
        }
    }

    int result = *min_element(dist[end].begin(), dist[end].end());
    if (result == numeric_limits<int>::max()) {
        cout << -1 << endl;
    } else {
        cout << result << endl;
    }

    return 0;
}