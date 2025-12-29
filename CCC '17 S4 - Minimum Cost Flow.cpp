#include <iostream>
#include <vector>
#include <sstream>
using namespace std;

typedef long long LL;

LL LSB(LL i) {
    return i & -i;
}

LL prefixSum(vector<vector<vector<LL>>>& tree3d, int x, int y, int z) {
    LL sum = 0;
    int tx, ty, tz;
    tz = z;
    while (tz > 0) {
        ty = y;
        while (ty > 0) {
            tx = x;
            while (tx > 0) {
                sum += tree3d[tz][ty][tx];
                tx -= LSB(tx);
            }
            ty -= LSB(ty);
        }
        tz -= LSB(tz);
    }
    return sum;
}

LL rangeQuery(vector<vector<vector<LL>>>& tree3d, int x1, int y1, int z1, int x2, int y2, int z2) {
    LL val1 = prefixSum(tree3d, x2, y2, z2)
             - prefixSum(tree3d, x1 - 1, y2, z2)
             - prefixSum(tree3d, x2, y1 - 1, z2)
             + prefixSum(tree3d, x1 - 1, y1 - 1, z2);

    LL val2 = prefixSum(tree3d, x2, y2, z1 - 1)
             - prefixSum(tree3d, x1 - 1, y2, z1 - 1)
             - prefixSum(tree3d, x2, y1 - 1, z1 - 1)
             + prefixSum(tree3d, x1 - 1, y1 - 1, z1 - 1);

    return val1 - val2;
}

void pointUpdate(vector<vector<vector<LL>>>& tree3d, int X, int Y, int Z, LL L, int N) {
    LL d = L - rangeQuery(tree3d, X, Y, Z, X, Y, Z);
    int tx, ty, tz;
    tz = Z;
    while (tz <= N) {
        ty = Y;
        while (ty <= N) {
            tx = X;
            while (tx <= N) {
                tree3d[tz][ty][tx] += d;
                tx += LSB(tx);
            }
            ty += LSB(ty);
        }
        tz += LSB(tz);
    }
}

int main() {
    int N, Q;
    cin >> N >> Q;
    cin.ignore(); // Ignore newline character

    vector<vector<vector<LL>>> tree3d(N + 1, vector<vector<LL>>(N + 1, vector<LL>(N + 1, 0)));

    LL s = 0;
    string line;

    for (int i = 0; i < Q; ++i) {
        getline(cin, line);
        stringstream ss(line);
        string cmd;
        ss >> cmd;

        if (cmd == "C") {
            int X, Y, Z;
            LL L;
            ss >> X >> Y >> Z >> L;
            pointUpdate(tree3d, X, Y, Z, L, N);
        } else if (cmd == "S") {
            int X1, Y1, Z1, X2, Y2, Z2;
            ss >> X1 >> Y1 >> Z1 >> X2 >> Y2 >> Z2;
            s += rangeQuery(tree3d, X1, Y1, Z1, X2, Y2, Z2);
        }
    }

    cout << s << endl;

    return 0;
}