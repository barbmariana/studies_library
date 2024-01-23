#include <signal.h>
#include <stdio.h>
#include<windows.h>

static void sig_handler(int sign)
{
        printf("Try again");
}

int     main(int argc, char *av)
{
        int j;
        if (signal(SIGINT, sig_handler) == SIG_ERR)
        {
                printf("error");
        }
        for(j = 0; ; j++)
        {
                printf("%d\n", j);
                sleep(3); // rest the program for 3 seconds
        }
}