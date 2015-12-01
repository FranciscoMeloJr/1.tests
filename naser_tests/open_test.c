#include <stdio.h>

int main() 
{
   int i =0;
   for(i = 0;i< 100; i++)
   {	   FILE *fp;
	   printf("Test open");
	   fp = fopen("test.txt", "w+");
	   fprintf(fp, "This is testing for fprintf...\n");
	   fputs("This is testing for fputs...\n", fp);
	   fclose(fp);
   }
}
