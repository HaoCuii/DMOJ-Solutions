/*
Notice how each square pool must either hit a tree or edge on the top and left sides of the square.
We can maintain a best square length (k), only around 500,000 operations because we don't check lower ones if we find a higher one
This way we can for each 2 trees we check the square of length k that has one tree at the top and on at the left, and see if it satisfies by checking all trees within that square\
If this tle we could optimize the check for newest big with binary search, right now it's just a +1
probably O(N + T^2)
*/

#include <bits/stdc++.h>
using namespace std;
int t,best,n;
int trees[105][5];

bool check(int x, int y, int l){
    for (int i = 0; i < t; i++){
        if ((trees[i][0] > x && trees[i][0] <= x+l && trees[i][1] > y && trees[i][1] <= y+l) || (x + l > n || y + l > n)){
            return false;
        }
    }
    return true;
}

int main(){
    cin >> n;
    cin >> t;
    for (int i = 0; i < t; i++){
        cin >> trees[i][0] >> trees[i][1];
    }
    trees[t][0] = 0;
    trees[t][1] = 0;
    t++; 
    best = 0;

    for (int i = 0; i < t; i++){
        for (int j = 0; j < t; j++){
            while (check(trees[i][0], trees[j][1], best + 1)){
                best++;
            }
        }
    }

    cout << best; 
    return 0;
}