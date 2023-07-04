LOGIC TO PRINT THE WORDS IN A SENTENCE IN REVERSE ORDER


LOGIC IN C
LOGIC-1
#include <stdio.h>
#include<string.h>

int main() {
   char s[100]="anusha is here";
   
  char w[20];
  int i,j;
  for(int i=strlen(s)-1,j=0;i>=0;i--){
      if(s[i]!=' '){
          w[j]=s[i];
          j++;
      }
      else{
          w[j]='\0';
          for(int k=strlen(w)-1;k>=0;k--){
              printf("%c",w[k]);
          }
          printf(" ");
          j=0;
      }
  }
  for(int k=strlen(w)-1;k>=0;k--){
              printf("%c",w[k]);
          }
}

OUTPUT:
here is anusha
--------------------------------------------------
LOGIC-2 IN C
#include <stdio.h>

void reverseIndiv(char s[], int start, int end) {
    while (start < end) {
        char temp = s[start];
        s[start] = s[end];
        s[end] = temp;
        start++;
        end--;
    }
}

void reverseWords(char s[], int len) {
    reverseIndiv(s, 0, len - 1);
    int start = 0;
    for (int i = 0; i < len; i++) {
        if (s[i] == ' ') {
            reverseIndiv(s, start, i - 1);
            start = i + 1;
        }
    }
    reverseIndiv(s, start, len - 1);
}

int main() {
    char s[] = "anusha is";
    int len = sizeof(s) / sizeof(char);
    reverseWords(s, len - 1);
    printf("%s", s);
    return 0;
}

OUTPUT:
is anusha