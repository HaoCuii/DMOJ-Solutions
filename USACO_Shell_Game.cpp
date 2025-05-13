#include <bits/stdc++.h>
using namespace std;

char shells[3] = {'a','b','c'};

int main(){
    ifstream fin("shell.in");
    ofstream fout("shell.out");

    int n; fin >> n;
    map<char,int> peb = {{'a',0},{'b',0},{'c',0}};
    for (int i = 0; i < n; i++){
        int a,b,g; fin >> a >> b >> g;
        a--; b--; g--; // convert to 0-based index
        char tempb = shells[b];
        shells[b] = shells[a];
        shells[a] = tempb;
        peb[shells[g]] += 1;
    }

    int big = 0;
    for (auto [key, val] : peb){
        big = max(big, val);
    }
    fout << big << "\n";
    return 0;
}
