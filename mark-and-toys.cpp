#include <bits/stdc++.h>

using namespace std;

const int MAXN = 1E5+3;
int a[MAXN], n, k;

int partition(int a[],int l,int  r) {
    int pivotId = (l + r) / 2;
    int pivot = a[pivotId];
    swap(a[pivotId], a[r]);
    int j = l - 1;
    for (int i=l; i<=r; i++) {
        if (a[i] <= pivot) {
            j++;
            swap(a[i], a[j]);
        }
    }
    return j;
}

void qs(int a[],int  l, int r) {
    if (r <= l) return;
    int index = partition(a, l, r);
    qs(a, l, index - 1);
    qs(a, index + 1, r);
}

int main() {
    cin >> n >> k;
    for (int i=0; i<n; i++) cin >> a[i];
    qs(a, 0, n-1);
    for (int i = 0; i < n; i++) cout << a[i] << " ";
    long long sum = 0;
    int res = 0;
    for (int i = 0; i < n; i++)
        if (sum + a[i] <= k) {
            sum += a[i];
            res ++;}
    cout << res;
    return 0;
}