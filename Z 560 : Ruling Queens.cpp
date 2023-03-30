#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
int sol[100][100];
bool issafe(int n,int r,int c){
    for(int i=r-1;i>=0;i--)if(sol[i][c])return 0;
    for(int i=r-1,j=c-1;i>=0 and j>=0;i--,j--)if(sol[i][j])return 0;
    for(int i=r-1,j=c+1;i>=0 and j<n;i--,j++)if(sol[i][j])return 0;
    return 1;
}
bool fillmaze(int n, int r){
    if(r==n)return true;
    for(int i=0;i<n;i++){
        if(issafe(n,r,i)){
            sol[r][i]=1;
            if(fillmaze(n,r+1))return true;
            sol[r][i]=0;
        }
    }
    return false;
}
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n; cin>>n;
    if(fillmaze(n,0)){
        for( int i=0; i<n;i++){
            for(int j=0;j<n;j++){
                cout<<sol[i][j]<<" ";
            }
            cout<<"\n";
        }
    }
    else cout<<"Not possible";
    return 0;
}
