#include <stdio.h>
#include <math.h>

int n, k;
int arr[505];

double preference(int s) 
{
    double sum1 = 0, sum2 = 0;
    for(int i = s; i < k + s; i++)
    {
        sum1 += (double)arr[i];
    }
    for(int i = s; i < k + s; i++)
    {
        sum2 += pow((double)(arr[i]-sum1/k),2.0); 
    }
    
    return sqrt(sum2/(double)k); 
}

int main()
{
    double mn = 9999999.0;
    scanf("%d %d", &n, &k);
    for(int i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }

    for(; k <= n; k++)
    {
        for(int i = 0; i <= n-k; i++)
        {
            double tmp = preference(i); 
            if(mn > tmp)
                mn = tmp; 
        }
    }
    printf("%0.11lf", mn);
    return 0;
}
