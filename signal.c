#include<stdio.h>
#include<signal.h>

void myhandle(int mysignal)
{
	printf("My handle %d\n", mysignal);
}
int main()
{
	int i = 0;
	signal(SIGTERM, myhandle);
	
	while(1)
	{
		printf("i=%d\n",i);
		i++;
		sleep(i);
	}
	return 0;
}

