// timed mode
#include <bits/stdc++.h>
using namespace std;



int main() {
  // n -> # of friends, k -> # of days until bday, d -> today
  int n,k,d,q; // q -> quarantine
  cin>>n>>k>>d;

  int cc = 0;
  for (int i = 0; i < n; i++) {
    cin>>q;
    if (q <= d) {
      cc++;
    }
  }

  return cc;
}
