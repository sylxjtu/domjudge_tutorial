#include<cstdio>
#include<string>
using namespace std;
typedef long long ll;
int n,i,len,f[1111111];
ll m;
bool check(){
    ll t=0;
    for(int i=len;i;i--)t=(t*10+f[i])%m;
    return t==0;
}
int main(){
    scanf("%d",&n);
    m=1LL<<n;
    if(n==1)return puts("12"),0;
    if(n==2)return puts("12"),0;
    f[1]=2;
    f[2]=1;
    len=2;
    for(int _=3;_<=n;_++){
        m=1LL<<_;
        len++;
        for(int i=1;i<=2;i++){
            f[len]=i;
            if(check())break;
        }
        if(!check())return puts("-1"),0;
    }
    for(int i=len;i;i--)printf("%d",f[i]);
}