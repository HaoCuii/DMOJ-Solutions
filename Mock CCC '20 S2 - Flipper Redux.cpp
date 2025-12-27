#include <bits/stdc++.h>
using namespace std;


//complete first column using row moves
//complete first row using column moves
//if the grid is not complete it means it's impossible
///idk proof 

int main(){
    int n; cin >> n;
    vector<vector<int>> grid(n, vector<int>(n));
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            cin >> grid[i][j];
        }
    }

    vector<string> moves;
    for (int i = 0; i < n; i++){
        if (grid[i][0] == 1){
            moves.push_back("R "+ to_string(i+1));
            for (int j = 0; j < n; j++){
                grid[i][j] = 1 - grid[i][j];
            }   
        }
    }

    for (int i = 0; i < n; i++){
        if (grid[0][i] == 1){
            moves.push_back("C " + to_string(i+1));
            for (int j = 0; j < n; j++){
                grid[j][i] = 1 - grid[j][i];
            } 
        }
    }

    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            if (grid[i][j] == 1){
                cout << -1;
                return 0;
            }
        }
    }


    cout << moves.size() << '\n';
    for (string s: moves){
        cout << s << "\n";
    }
    
    return 0;
}