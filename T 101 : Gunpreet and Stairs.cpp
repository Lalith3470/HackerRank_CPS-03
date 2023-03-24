#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n;cin>>n;
    if(n<=2)cout<<n;
    else if(n==3)cout<<4;
    else{
        long int a=1,b=2,c=4,res;
        for(int i=4;i<=n;i++){
            res=a+b+c;
            a=b;b=c;c=res;
        }
        cout<<res;
    }
    return 0;
}
