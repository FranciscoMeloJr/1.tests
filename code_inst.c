#include<stdio.h>

int addnum(int a, int b)
{
	int sum=0;
#ifdef INSTDEBUG
	printf("Debug:%d %d", a, b);	
#endif
	sum = a + b;

#ifdef INSTDEBUG
        printf("Debug:%d", sum);
#endif

	return sum;
}
int main(int argc, char**argv)
{
	int total;
	
	total = addnum(atoi(argv[1]),atoi(argv[2]));
	printf("Total %d\n", total);
	return 0;
}
