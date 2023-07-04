//maximum palindrome
#include<stdio.h>
int main()
{
    int number[] = {121,6886,2,829272628,0101};
    int n=sizeof(number)/sizeof(number[0]);
    int max_palindrome=0;
    for(int i=0;i<n;i++){
        int reverse_num=0;
        int num=number[i];
        int original_num=number[i];
        while(num!=0){
            int remainder=num%10;
            reverse_num=reverse_num*10+remainder;
            num /=10;
        }
        if(original_num==reverse_num){
           if(original_num>max_palindrome){
               max_palindrome=original_num;
           }
        }
    }
    if(max_palindrome==0){
        printf("no palindrome found\n");
    }
    else{
        printf("maximum palindrome number is: %d\n",max_palindrome);
    }
    return 0;
}
