
/* Header Files */
#include <stdlib.h>
#include <stdio.h>
#include <math.h>


/* Function Prototypes */
void fibo(int n);
int divBy_op(int b);
int primeCheck(int b);


/* main function to call Fibonacci Sequence Generator */
// This is where the testing takes place
void main()
{
    int totalNumber = 0;
    printf("Enter the number of fibonacci numbers required:\n");
    scanf ("%d", &totalNumber);
    if (totalNumber < 2)
    printf ("please input a number greater than 2");
    else
    printf("Fibonacci Sequence \n");
    fibo(totalNumber);
}


/* Function Declarations*/

void fibo(int n){

    int a = 0;
    int b = 1;
    int i = 0;
    //printf("%i \n",1);  // 1 is the chosen Starting point of the Sequence

    for  (i = 0; i < (n - 1); i++) {
        int t = a;
        a = b;
        b += t;     // b = F(n): is the latest number of the Fib Sequence being generated

        if( primeCheck(b) ) {}  // Checks if b is divisible by 3 or 5
        else if( divBy_op(b) ) {}  // Checks if b is prime
        else {
            printf("%i \n",b);
        }

    }
//    return b;
}

int divBy_op(int b){

    if (b % 3 == 0){
        printf("Buzz \n");
        return 1;
    }
    if(b % 5 == 0){
        printf("Fizz \n");
        return 1;
    }
    return 0;
}

int primeCheck(int b){

    int c;

   for ( c = 2 ; c <= b/2 ; c++ ){
        if (b % c == 0 )
        return 0;
       //printf("BuzzFizz\n");
   }
   printf("BuzzFizz\n");
   return 1;
}

