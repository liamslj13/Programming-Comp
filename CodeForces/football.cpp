#include <iostream>
using namespace std;

int main() {
  string word;
  bool b=false;
  int sum = 1;
  cin>>word;
  int len = word.length();

  if (len < 7) {
    cout<<"NO"<<endl;
    return 0;
  }

  for (int i = 1; i<len;i++) {
    if (word[i] == word[i-1]) {
      sum++;
    } else {
      sum = 1;
    }

    if (sum == 7) {
        cout<<"YES"<<endl;
        b = true;
        break;
    }
  }
  if (!b) {
      cout<<"NO"<<endl;
  }

  return 0;
}
