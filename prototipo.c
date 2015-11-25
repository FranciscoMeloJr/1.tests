#include <stdio.h>

//Prototype:
int main(void) 
{

   FILE *fp;
   char buff[255];

   int i = 0;
   for(i = 0; i< 1000; i++)
   {
   fp = fopen("test23.txt", "r");
   fscanf(fp, "%s", buff);
   printf("1 : %s\n", buff );

   
   fclose(fp);
   }
   return 0; 
}
