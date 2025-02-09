#include <stdio.h>
#include <string.h>

int main(){
    char input[100];
    printf("Please enter key: ");
    scanf("%s", input);
    if (strcmp("__stack_check", input))
    {
        printf("Nope.\n");
    }
    else
    {
        printf("Good job!\n");
    }
    return 0;
}