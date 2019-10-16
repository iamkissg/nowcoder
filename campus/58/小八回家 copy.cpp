#include<iostream>

using namespace std;

int go_home(int n){
    if(n == 1){
        return 1;
    }
    if(n == 2){
        return 2;
    }
    
    int a = 1;
    int b = 2;
    int tmp = 0;
    for(int i=2; i<n; i++){
        tmp = a;
        a = b;
        b = tmp + a;
    }
    return b;
}
int main(int argc, char const *argv[])
{
    
    int n;
    cin>>n;
    cout<<go_home(n);
    return 0;
}
