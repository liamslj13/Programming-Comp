#include <iostream>
#define ll long long
using namespace std;

int main() {
    int A,B,C,D,count=0;
    cin>>A>>B>>C>>D;
    ll total = B;

    while (total % C != 0 && total % D != 0) {
        total--;
        cout<<total<<" ";
    }

    while (total >= A) {
        if (total % C == 0 && total % D == 0 && total >= A) {
            count++;
        }
        total -= D;
    }

    cout<<count<<endl;
    return 0;
}
