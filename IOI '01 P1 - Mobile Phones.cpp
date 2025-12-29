#include <iostream>
#include <vector>

using namespace std;

vector<vector<int>> tree2d;
int N;

int LSB(int i) {
    return i & -i;
}

int prefixSum(int x, int y) {
    int sum = 0;
    while (y > 0) {
        int tx = x;
        while (tx > 0) {
            sum += tree2d[y][tx];
            tx -= LSB(tx);
        }
        y -= LSB(y);
    }
    return sum;
}

int rangeQuery(int x1, int y1, int x2, int y2) {
    return (prefixSum(x2, y2) 
            - prefixSum(x1 - 1, y2) 
            - prefixSum(x2, y1 - 1) 
            + prefixSum(x1 - 1, y1 - 1));
}

void pointUpdate(int x, int y, int a) {
    while (y <= N) {
        int tx = x;
        while (tx <= N) {
            tree2d[y][tx] += a;
            tx += LSB(tx);
        }
        y += LSB(y);
    }
}

int main() {
    int x;
    cin >> x >> N;

    tree2d = vector<vector<int>>(N + 1, vector<int>(N + 1, 0));

    while (true) {
        int type;
        cin >> type;
        if (type == 3) {
            break;
        }

        if (type == 1) {
            int X, Y, A;
            cin >> X >> Y >> A;
            pointUpdate(X + 1, Y + 1, A);
        } else if (type == 2) {
            int L, B, R, T;
            cin >> L >> B >> R >> T;
            cout << rangeQuery(L + 1, B + 1, R + 1, T + 1) << endl;
        }
    }

    return 0;
}