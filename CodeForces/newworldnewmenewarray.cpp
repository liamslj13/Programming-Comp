#include <iostream>
using namespace std;


int main() {
  int t,n,k,p,sum,count;
  bool neg = false;
  cin>>t;
  for (int i = 0; i<t;i++) {
      cin>>n>>k>>p;
      sum = 0;
      count = 0;
      if (k < 0) {neg = true;}
      if (neg) {
        while (sum > k) {
          sum -= p;
          count++;
        }
      } else {
        while (sum < k) {
          sum += p;
          count++;
        }
      }

      if (count > n) {
        cout<<-1<<endl;
      } else {
        cout<<count<<endl;
      }
      neg = false;
  }

  return 0;
}
