#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

void no()
{
    printf("Nope\n");
    exit(1);
}

void ok()
{
    printf("Good job!\n");
    exit(0);
}

int main()
{
    int count_input;
    char input[24];
    char passwd[9];
    char pw[4];
    int passwd_idx;
    int input_idx;
    size_t passwd_len;
    bool is_run;
    int ascii_num;

    printf("please enter key: ");
    count_input = scanf("%s", input);
    input[23] = 0;

    if (count_input != 1)
        no();
    if (input[1] != '0')
        no();
    if (input[0] != '0')
        no();

    fflush(stdin);

    memset(passwd, 0, 9);
    passwd[0] = 'd';
    pw[3] = 0;
    passwd_idx = 1;
    input_idx = 2;

    while(true)
    {
        passwd_len = strlen(passwd);
        is_run = false;
        if (passwd_len < 8)
        {
            passwd_len = strlen(input);
            is_run = input_idx < passwd_len;
        }
        if (!is_run) break;
        pw[0] = input[input_idx];
        pw[1] = input[input_idx + 1];
        pw[2] = input[input_idx + 2];
        ascii_num = atoi(pw);
        passwd[passwd_idx] = (char)ascii_num;
        input_idx += 3;
        passwd_idx++;
    }
    passwd[passwd_idx] = 0;
    if (strcmp(passwd, "delabere") != 0)
        no();
    else
        ok();   
    return 0;
}
