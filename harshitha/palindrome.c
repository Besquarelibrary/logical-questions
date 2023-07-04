//string is palindrome or not
#include<stdio.h>
#include<string.h>
int main(){
	int i,len;
	char str[100];
	printf("enter the sring:");
	scanf("%s",str);
	len=strlen(str);
	for(i=0;i<=len/2;i++){
		if(str[i]!=str[len-i-1]){
			printf("%s is not a palindrome",str);
			return 0;
		}
		else{
			printf("%s is a palindrome",str);
			return 0;
		}
		
	}

	
	
}
