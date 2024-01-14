#include<bits/stdc++.h>
using namespace std;
int main(){
    vector<int> vec={1,2,2,2,3,3,4,66,66,78,79,89,689};
    auto it=upper_bound(vec.begin(),vec.end(),66);
    int index=it-vec.begin()-1;
    cout<<index;
}