#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>



void doSomeWork(int i);
int main(int argc, char * argv[])
{
	printf("I am %d", (int) getpid());
	
	//sleep(1);
	pid_t pid=fork();
	printf("fork returned %d", (int)pid);
	
	if(pid<0)
	{
		perror("Fork failed");
	}
	if(pid==0) //child
	{
		printf("Im the child");
		doSomeWork(3);
		exit(47);
	}
//	if(pid>0) //parent
//	{		
//	}
	
	int status = 0;
	printf("\nI am the parent, waiting for child to end\n");
	pid_t childpid = wait(&status); //put the result in status &
	int childreturn = WEXITSTATUS(status);
	printf("\nParent ending.\n, return child: %d", childreturn);

	return 0;
}

//do something:
void doSomeWork(int i)
{
	const int NUM_TIMES=5;
	int t;
	for(t=0;t < NUM_TIMES; t++)
	{	
		//sleep(rand() % 4);
	}
	return;
}
