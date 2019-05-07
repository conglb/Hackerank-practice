#include <bits/stdc++.h>

using namespace std;

const int hx[6] = {-2, -2, 0, 2, 2, 0};
const int hy[6] = {-1, 1, 2, 1, -1, -2};
const string code[] = {"UL", "UR", "R", "LR", "LL", "L"};

int n, sx, sy, tx, ty, ans, ansvec[100003];
vector<int> vec;

int cost(int x, int y) { return abs(x - tx) + abs(y - ty); }

bool onBoard(int x, int y) { return x >= 0 && y >= 0 && x < n && y < n; }

bool travesal(int x, int y) {
    if (vec.size() == ans) {
        return false;
    }
  if (x == tx && y == ty) {
      if (ans > vec.size()) {
          ans = vec.size();
          for (int i=0; i<vec.size(); i++) ansvec[i] = vec[i];
      }
      return true;
  }
  bool check = false;
  for (int i = 0; i < 6; i++) {
    int u = x + hx[i], v = y + hy[i];
    //cout << u << v << endl;
    if (onBoard(u, v)) {
      if (cost(u, v) < cost(x, y)) {
        vec.push_back(i);
        if (travesal(u, v))
          check = true;
        vec.pop_back();
      }
    }
  }
  return check;
}

int main() {
  cin >> n;
  cin >> sx >> sy;
  cin >> tx >> ty;

  ans = 2*n;
  if (travesal(sx, sy)) {
    cout << ans << endl;
    for (int i=0; i<ans; i++)
      cout << code[ansvec[i]] << " ";
  } else cout << "Impossible";
  return 0;
}
