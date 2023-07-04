//reverse the vowels
#include <stdio.h>
#include <string.h>

int main()
{
    char str[] = "hello hii";
    char str2[100] = "";
    int len = strlen(str);
    int j = 0;

    printf("Original string: %s\n", str);

    for (int i = 0; i < len; i++)//looping to copy the vowels in the string
    {
        if (str[i] == 'a' || str[i] == 'e' || str[i] == 'i' || str[i] == 'o' || str[i] == 'u' ||
            str[i] == 'A' || str[i] == 'E' || str[i] == 'I' || str[i] == 'O' || str[i] == 'U') //condition for a vowel
        {
            str2[j] = str[i];
            j++;
        }
    }

    str2[j] = '\0';

    printf("Vowel string: %s\n", str2);

    j--;

    for (int i = 0; i < len; i++) //to replace the reversed vowels
    {
        if (str[i] == 'a' || str[i] == 'e' || str[i] == 'i' || str[i] == 'o' || str[i] == 'u' ||
            str[i] == 'A' || str[i] == 'E' || str[i] == 'I' || str[i] == 'O' || str[i] == 'U') 
        {
            str[i] = str2[j];
            j--;
        }
    }

    printf("String with reversed vowels: %s\n", str);

    return 0;
}
