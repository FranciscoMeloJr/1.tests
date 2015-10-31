#include<stdio.h>

#define NUM1 3
#define NUM2 5

/*This is may comment*/
#define SUM(x,y) x+y
int main(int argc, char* argv[])
{
	int i;
	int k;
	
	int sum;

        i = NUM1;
	k = NUM2;

	sum =SUM(NUM1,NUM2);

	/* This is my comment*/
	return 0;
}
