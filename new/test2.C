#include <iostream>


void foo()
{
	int i; //counter
	do{
		//nothing		
	}while(i<1000);

	return;
}
void bar()
{
        int i; //counter
        do{
                //nothing               
        }while(i<1000);

        return;
}

void baz()
{
        int i; //counter
        do{
                //nothing               
        }while(i<1000);

        return;
}

int main()
{
    std::cout<<"Hello World!\n";
    foo();
    bar();
    baz();
    return 0;
}

