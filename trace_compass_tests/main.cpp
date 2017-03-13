#include <iostream>
using namespace std;

int exp(float base, int exponent){
  
    //cout << base << "^" << exponent << " = ";
   //int exponent;
   //float base, 
   float result = 1;

    while (exponent != 0) {
        result *= base;
        --exponent;
    }

    cout << result;

   return result;
}
int main() 
{
    int exponent;
    float base, result = 1;

    
    cin >> base >> exponent;
    result = exp(base, exponent);
    cout << result;
    
    return 0;
}
