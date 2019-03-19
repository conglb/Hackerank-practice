#include <bits/stdc++.h>

using namespace std;

const int oo = 1234567890;

int main() {
	int n, m, x, y, r, start;
	vector<pair<int,int> > adj[3000];
	cin >> n >> m;
	for (int i = 1; i <= m; i ++) {
		cin >> x >> y >> r;
		adj[x].push_back(make_pair(y, r));
		adj[y].push_back(make_pair(x, r));
	}
	cin >> start;
	int d[n+1], ans = 0;
	bool mark[n+1];
	for (int i=1; i <= n; i++)  {
		d[i] = oo; mark[i] = 0;
	}
	d[start] = 0;
	while (true) {
		int id = 0;
		for (int i=1; i<=n; i++) 
			if (!mark[i]) {
				if (id == 0) {
					id = i;
				} else if (d[i] < d[id]) {
					id = i;
				}
			}
		//cout << d[id] << endl;
		if (!id) break;
		mark[id] = 1;
		ans += d[id];
		d[id] = 0;
		for (auto e: adj[id]) {
			int u = id;
			int v = e.first;
			int c = e.second;
			if (!mark[v]) {
				if (c < d[v]) {
					d[v] = c;
					//ans += c;
				}
			}
		}
	}
	cout << ans;
}