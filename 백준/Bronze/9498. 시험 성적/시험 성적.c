#include<stdio.h>
int main(){
    int score;
    scanf("%d",&score);
    if(score>89 && score<101){
        printf("A");
    }else if(score>79 && score<90){
        printf("B");
    }else if(score>69 && score<80){
        printf("C");
    }else if(score>59 && score<70){
        printf("D");
    }else{
        printf("F");
    }
}
