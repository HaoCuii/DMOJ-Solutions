#include <bits/stdc++.h>
using namespace std;

const int MAXN = 100005;

int n, m, arr[MAXN];
int minTree[4 * MAXN], gcdTree[4 * MAXN];
map<int, int> freqTree[4 * MAXN];

// MIN SEGMENT TREE
void buildMin(int v, int tl, int tr) {
    if (tl == tr) {
        minTree[v] = arr[tl];
    } else {
        int tm = (tl + tr) / 2;
        buildMin(v*2, tl, tm);
        buildMin(v*2+1, tm+1, tr);
        minTree[v] = min(minTree[v*2], minTree[v*2+1]);
    }
}

void updateMin(int v, int tl, int tr, int pos, int val) {
    if (tl == tr) {
        minTree[v] = val;
    } else {
        int tm = (tl + tr) / 2;
        if (pos <= tm) updateMin(v*2, tl, tm, pos, val);
        else updateMin(v*2+1, tm+1, tr, pos, val);
        minTree[v] = min(minTree[v*2], minTree[v*2+1]);
    }
}

int queryMin(int v, int tl, int tr, int l, int r) {
    if (l > r) return INT_MAX;
    if (l == tl && r == tr) return minTree[v];
    int tm = (tl + tr) / 2;
    return min(queryMin(v*2, tl, tm, l, min(r, tm)),
               queryMin(v*2+1, tm+1, tr, max(l, tm+1), r));
}

// GCD SEGMENT TREE
void buildGCD(int v, int tl, int tr) {
    if (tl == tr) {
        gcdTree[v] = arr[tl];
    } else {
        int tm = (tl + tr) / 2;
        buildGCD(v*2, tl, tm);
        buildGCD(v*2+1, tm+1, tr);
        gcdTree[v] = __gcd(gcdTree[v*2], gcdTree[v*2+1]);
    }
}

void updateGCD(int v, int tl, int tr, int pos, int val) {
    if (tl == tr) {
        gcdTree[v] = val;
    } else {
        int tm = (tl + tr) / 2;
        if (pos <= tm) updateGCD(v*2, tl, tm, pos, val);
        else updateGCD(v*2+1, tm+1, tr, pos, val);
        gcdTree[v] = __gcd(gcdTree[v*2], gcdTree[v*2+1]);
    }
}

int queryGCD(int v, int tl, int tr, int l, int r) {
    if (l > r) return 0;
    if (l == tl && r == tr) return gcdTree[v];
    int tm = (tl + tr) / 2;
    return __gcd(queryGCD(v*2, tl, tm, l, min(r, tm)),
                 queryGCD(v*2+1, tm+1, tr, max(l, tm+1), r));
}

// FREQUENCY SEGMENT TREE
void buildFreq(int v, int tl, int tr) {
    if (tl == tr) {
        freqTree[v][arr[tl]] = 1;
    } else {
        int tm = (tl + tr) / 2;
        buildFreq(v*2, tl, tm);
        buildFreq(v*2+1, tm+1, tr);
        freqTree[v].clear();
        for (auto &p : freqTree[v*2])
            freqTree[v][p.first] += p.second;
        for (auto &p : freqTree[v*2+1])
            freqTree[v][p.first] += p.second;
    }
}

void updateFreq(int v, int tl, int tr, int pos, int oldVal, int newVal) {
    if (tl == tr) {
        freqTree[v][oldVal]--;
        if (freqTree[v][oldVal] == 0)
            freqTree[v].erase(oldVal);
        freqTree[v][newVal]++;
    } else {
        int tm = (tl + tr) / 2;
        if (pos <= tm) updateFreq(v*2, tl, tm, pos, oldVal, newVal);
        else updateFreq(v*2+1, tm+1, tr, pos, oldVal, newVal);
        freqTree[v].clear();
        for (auto &p : freqTree[v*2])
            freqTree[v][p.first] += p.second;
        for (auto &p : freqTree[v*2+1])
            freqTree[v][p.first] += p.second;
    }
}

int queryFreq(int v, int tl, int tr, int l, int r, int val) {
    if (l > r) return 0;
    if (l == tl && r == tr) {
        auto it = freqTree[v].find(val);
        if (it != freqTree[v].end()) return it->second;
        return 0;
    }
    int tm = (tl + tr) / 2;
    return queryFreq(v*2, tl, tm, l, min(r, tm), val) +
           queryFreq(v*2+1, tm+1, tr, max(l, tm+1), r, val);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> m;
    for (int i = 0; i < n; ++i)
        cin >> arr[i];

    buildMin(1, 0, n-1);
    buildGCD(1, 0, n-1);
    buildFreq(1, 0, n-1);

    while (m--) {
        char op; cin >> op;
        if (op == 'C') {
            int x, v; cin >> x >> v; x--;
            int oldVal = arr[x];
            arr[x] = v;
            updateMin(1, 0, n-1, x, v);
            updateGCD(1, 0, n-1, x, v);
            updateFreq(1, 0, n-1, x, oldVal, v);
        } else {
            int l, r; cin >> l >> r; l--; r--;
            if (op == 'M') {
                cout << queryMin(1, 0, n-1, l, r) << '\n';
            } else if (op == 'G') {
                cout << queryGCD(1, 0, n-1, l, r) << '\n';
            } else if (op == 'Q') {
                int g = queryGCD(1, 0, n-1, l, r);
                cout << queryFreq(1, 0, n-1, l, r, g) << '\n';
            }
        }
    }

    return 0;
}
