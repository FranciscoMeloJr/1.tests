#include<stdio.h>
#include<string.h>

/*Comment*/
int main(int argc, char *argv[])
{
	//variables
	char str[24];
	char str2[24];
	int i;
	
	/*Example 1*/
	sprintf(str,"Hello world");//send to a variable
	
	printf("%s\n",str);
	/*Example 2*/
	i=4;
	sprintf(str, "Value of i= %d",i);
	printf("%s\n", str);

	/*Example 3*/
	strcpy(str2, str);
	printf("str2 is %s", str2);
	
	/*Example 4*/
	memset(str, 0,24);
	memset(str,'a',10 );
	printf(">%s<",str);

	return 0;
}
