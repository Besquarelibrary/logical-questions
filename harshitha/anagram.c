#include<stdio.h>
#include<string.h>
int main(){
int i,j,len1,len2,count=0;
char s1[100],s2[100];
printf("enter first string:");
gets(s1);
printf("enter second string:");
gets(s2);
len1=strlen(s1);
len2=strlen(s2);
if(len1==len2){
	for(i=0;i<len1;i++){
		for(j=0;j<len2;j++){
			if(s1[i]==s2[j]){
				count++;
				break;
			}
		}
	}
	if(count==len1){
		printf("the strings are anagram");
	}
	}
	else{
		printf("strings are not anagram");
	return 0;
}
}
