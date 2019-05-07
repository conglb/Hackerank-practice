#include <bits/stdc++.h>
using namespace std;

int d[100], n;
string s;
int main() {
    cin >> s;
    n = s.length();
    for (int i=0; i<n; i++) d[s[i] - 'a'] ++;
    int ma = 0;
    for (int i=0; i<26; i++) ma = max(d[i], ma);
    if (ma == 1) {
        cout << "YES";
        return 0;
    }
    /* id is popular */
    int id;
    for (id = 0; id < 26; id++) {
        if (d[id] > 1) break;
    }
    /* if all equal id-1 */
    bool check = 1;
    for (int i=0; i<26; i++) if (d[i] != 0 && i != id && d[id] - 1 != d[i]) check = 0;
    if (check) {
        cout << "YES";
        return 0;        
    }

    bool secondChance = true;
    for (int i=0; i < 26; i++) 
    if (d[i] != d[id] && d[i] != 0)
    {
        if (d[i] == 1 || d[i] - d[id] == 1) {
            if (secondChance) secondChance = false; else {
                cout << "NO";
                return 0;
            }
        }  else {
            cout << "NO";
            return 0;
        }
    }
    cout << "YES";
    return 0;
}