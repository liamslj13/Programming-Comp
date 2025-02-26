#include <iostream>
using namespace std;

int main() {
  int n,p,v,t,sum,res=0;
  cin>>n;

  for (int i = 0;i<n;i++) {
    sum = 0;
    cin>>p>>v>>t;
    if (p+v+t>=2) {
      res++;
    }
  }

  cout<<res<<endl;
  return 0;
}
