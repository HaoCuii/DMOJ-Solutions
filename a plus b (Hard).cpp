#include <bits/stdc++.h>
using namespace std;

string add(string a, string b){
    int na = a.size(), nb = b.size(), carry = 0;
    string c;
    int i = na-1, j = nb-1;
    while (i >= 0 || j >= 0 || carry) {
        int da = (i >= 0 ? a[i--] - '0' : 0);
        int db = (j >= 0 ? b[j--] - '0' : 0);
        int sum = da + db + carry;
        c.push_back(char('0' + (sum % 10)));
        carry = sum / 10;
    }
    reverse(c.begin(), c.end());
    return c;
}

string subtract(string a, string b){
    int na = a.size(), nb = b.size(), borrow = 0;
    string c;
    int i = na-1, j = nb-1;
    while (i >= 0) {
        int da = a[i] - '0' - borrow;
        int db = (j >= 0 ? b[j] - '0' : 0);
        if (da < db) {
            da += 10;
            borrow = 1;
        } else {
            borrow = 0;
        }
        c.push_back(char('0' + (da - db)));
        i--; j--;
    }
    while (c.size() > 1 && c.back() == '0') 
        c.pop_back();
    reverse(c.begin(), c.end());
    return c;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n; 
    cin >> n;
    while (n--) {
        string a, b;
        cin >> a >> b;
        bool na = (a[0]=='-'), nb = (b[0]=='-');
        if (na) a = a.substr(1);
        if (nb) b = b.substr(1);

        string result;
        if (na == nb) {
            result = add(a, b);
            if (na) result.insert(result.begin(), '-');
        } else {
            bool a_ge_b = (a.size() > b.size() || (a.size()==b.size() && a >= b));
            if (a_ge_b) {
                result = subtract(a, b);
                if (na) result.insert(result.begin(), '-');
            } else {
                result = subtract(b, a);
                if (!na) result.insert(result.begin(), '-');
            }
        }

        if (result == "-0"){
            result = '0';
        }
        cout << result << "\n";
    }
    return 0;
}
