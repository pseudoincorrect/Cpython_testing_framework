#include "heart_rate.h"

#define ARR_LEN 10

int main (int argc, char* argv[])
{
    int32_t in_data[ARR_LEN] = { 3095776, 3095764, 3095795, 3095803, 3095743, 3095650, 3095593, 3095588, 3095635, 3095698 };
    int32_t out_data[ARR_LEN] = {0};

    heart_rate_init();

    for(int i = 0; i <ARR_LEN; i++)
    {
        out_data[i] = heart_rate_process(in_data[i]);
        printf("in_data[i]= %d   out_data[i]=%d \n\r",in_data[i], out_data[i]);
    }
}