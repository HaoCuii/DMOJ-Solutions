#include <iostream>
using namespace std;

int main(){
    string s;
    string t;
    int k;
    getline(cin,s);
    getline(cin,t);
    cin >> k;

    int ans = 0;
    for (int i = 0; i < s.length(); i++){
        if ((s[i] == ' ' & t[i] != ' ') or (t[i] == ' ' & s[i] != ' ')){
            cout << "No plagiarism";
            return 0;
        }
        if (s[i] != t[i] ) {
            ans += 1;
        }
    }

    if (ans > k) {
        cout << "No plagiarism";
    }
    else {
        cout << "Plagiarized";
    }
    return 0;
}