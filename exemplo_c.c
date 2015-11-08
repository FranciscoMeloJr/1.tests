#include <stdlib.h>
#include <stdio.h>
#include "tp.h"

#define TRACEPOINT_CREATE_PROBES
#define TRACEPOINT_DEFINE


/* ... */

int main(void)
{
    struct stat s;

    stat("/etc/fstab", &s);

    tracepoint(my_provider, my_tracepoint, 23, "Hello, World!", &s);

    return 0;
}
