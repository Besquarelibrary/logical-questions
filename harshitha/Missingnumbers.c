//missing numbers
#include <stdio.h>

int main() {
    int arr[] = {1,3,5,9,10,12,13,14}; 
    int n = sizeof(arr) / sizeof(int);
    int n_number = 20;
    int count[n_number] ;
    int i;

    for (i = 0; i < n; i++) { // loop for assign values to count array
        count[arr[i]]++;
    }

    for (i = 0; i < n_number; i++)  //looping to find thee missing element
{ 
        if (count[i] == 0) // condition for missed elemnt 
{ 
            printf("%d is missing.\n", i);
        }
    }

    return 0;
}

