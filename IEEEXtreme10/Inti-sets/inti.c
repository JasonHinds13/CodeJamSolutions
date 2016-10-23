#include <stdio.h>

long gcd(long x, long y){

    while (x * y != 0) {
        if (x >= y) x = x % y;
        else y = y % x;
    }
    return (x + y);
}

long sum_inti(long n, long a, long b){

    long sum = 0;

    for(int i=a; i <= b; i++)
        if (gcd(n,i) == 1) sum = sum + i;
        
    return sum;
}

int main(){
    int q;

    scanf("%d",&q);

    for(int i=0; i < q; i++){
        int n,a,b;

        scanf("%d %d %d",&n,&a,&b);

        long res = sum_inti(n,a,b) % 1000000007;

        printf("%ld\n", res);
    }
    
    return 0;
}
