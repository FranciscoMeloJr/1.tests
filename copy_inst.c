#include<stdio.h>

int addnum(int a, int b)
{
	int sum=0;
#ifdef INSTDEBUG
	printf("Debug:%s %d", __FILE__, __LINE__);	
#endif
	sum = a + b;

#ifdef INSTDEBUG
        printf("Debug:%s %d ", __FILE__, __LINE__);
#endif

	return sum;
}

int main()
{
	int total;
	
	total = addnum(4,5);
	printf("Total %d\n", total);
	return 0;
}
