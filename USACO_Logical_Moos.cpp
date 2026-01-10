#include <bits/stdc++.h>
using namespace std;

struct Node{
    string b;
    int left;
    int right;
};

int main(){
    int n, q; 
    cin >> n >> q;
    vector<string> lis(n);
    for (int i = 0; i < n; i++){
        cin >> lis[i];
    }

    vector<int> psa(n);
    for (int i = 0; i < n; i++){
        int val = 0;
        if (lis[i] == "false") {
            val = 1;
        }

        if (i == 0) {
            psa[i] = val;
        } else {
            psa[i] = psa[i-1] + val;
        }
    }

    vector<Node> ors;
    vector<int> id(n); 

    string curr = "true";
    int l = 0;
    int trues = 0;
    int falses = 0;
    
    for (int i = 0; i < n; i++){
        if (lis[i] == "or") {
            ors.push_back({curr, l, i - 1}); 
            for (int j = l; j <= i - 1; j++) {
                id[j] = ors.size() - 1;
            }

            l = i + 1; 
            if (curr == "true"){
                trues++;
            }
            else{
                falses++;
            }
            curr = "true"; 
        }
        else if (lis[i] == "false"){
            curr = "false";
        }
    }

    ors.push_back({curr, l, n - 1});
    if (curr == "true") trues++;
    else falses++;

    for (int j = l; j < n; j++) {
        id[j] = ors.size() - 1;
    }
    
    vector < int > chunk_psa(ors.size());
    for (int i = 0; i < ors.size(); i++) {
        int val = 0;
        if (ors[i].b == "true") {
            val = 1;
        }
        if (i == 0) {
            chunk_psa[i] = val;
        } else {
            chunk_psa[i] = chunk_psa[i - 1] + val;
        }
    }

    int x, y;
    string boo;
    string ans = "";
    for (int i = 0; i < q; i++){
        cin >> x >> y >> boo;
        x--; y--;
        //subtracting
        int removed_trues = chunk_psa[id[y]];
        if (id[x] > 0) {
            removed_trues -= chunk_psa[id[x] - 1];
        }
        //adding back lost
        bool new_chunk = true;
        if (x > ors[id[x]].left){
            int is_false = psa[x - 1];
            if (ors[id[x]].left > 0){
                is_false -= psa[ors[id[x]].left - 1];
            }  
            if (is_false != 0){
                new_chunk = false;
            }
        }
        if (y < ors[id[y]].right){
            int is_false = psa[ors[id[y]].right] - psa[y];
            if (is_false != 0){
                new_chunk = false;
            } 
        }

        //FINALY STEP 
        int current_trues = trues - removed_trues;
        if (boo == "false"){
            if (current_trues > 0){
                ans += "N";
            }
            else{
                ans += "Y";
            }
        }
        else{
            if (current_trues > 0 || (new_chunk == true && current_trues+1 > 0)){
                ans += "Y";
            }
            else{
                ans += "N";
            }
        }
    } 

    cout << ans;
    return 0;
}