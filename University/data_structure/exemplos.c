#include <stdio.h>

int     func_len(int *arr)
{
        int     i;

        i = 0;
        while (arr[i])
        {
                i++;
        }
        return i;
}
void    func_rev(int arr[])
{
        int     i;
        int     len;
        int     temp;
        int     n;

        i = 0;
        len = func_len(arr) - 1;
        while (i < len/2)
        {
                temp = arr[i];
                arr[i] = arr[len - i];
                arr[len - i] = temp;
                i++;

        }

}
int     main(void)
{
        int arr[] = {1,2,3,4,5, '\0'};
        func_rev(arr);
        printf("%d%d%d%d%d", arr[0], arr[1], arr[2], arr[3], arr[4], arr[5]);

}