/* Header Files */
#include <stdlib.h>
#include <stdio.h>
#include <math.h>

/////////////////////

/* Function Prototypes */
void fibo(int n);
int divBy_op(int b);
int primeCheck(int b);


/////////////////////


/* main function to call Fibonacci Sequence Generator */
// This is where the testing takes place
void main()
{
    int totalNumber = 0;
    printf("Enter the number of Fibonacci numbers required:\n");
    scanf ("%d", &totalNumber);
    if totalNumber < 2
    print ("please input a number greater than 2");
    else
    printf("Fibonacci Sequence \n");
    fibo(totalNumber);
}

/////////////////////

/* Function Declarations*/

void fibo(int n){
///////////////////////////////////////////////////////////////////////
// Purpose:    Generates Fibonacci Sequence
// Input:   n
// Returns:   Nothing / void
// Calls:  checkDivisible(), checkPrime();
// Notes:  printing the value F(n) when not prime or divisible be 3 or 5.
///////////////////////////////////////////////////////////////////////
    int a = 0;
    int b = 1;
    int i = 0;
    //printf("%i \n",1);  // 1 is the chosen Starting point of the Sequence

    for  (i = 0; i < (n - 1); i++ {
        int t = a;
        a = b;
        b += t;     // b = F(n): is the latest number of the Fib Sequence being generated

        if( divBy_op(b) ) {}  // Checks if b is divisible by 3 or 5
        else if( primeCheck(b) ) {}  // Checks if b is prime
        else {
            printf("%i \n",b);
        }

    }
//    return b;
}

int divBy_op(int b){
///////////////////////////////////////////////////////////////////////
// Purpose:   Checks if the number is divisible by 3 or 5
// Input:     b
// Returns:   True(1) if input is divisible by 3 or 5. False(0) otherwise.
// Notes:     prints ...
// ... "Buzz" when b is divisible by 3.
// ... "Fizz" when b is divisible by 5.
///////////////////////////////////////////////////////////////////////
    if (b%3 == 0){
        printf("Buzz \n");
        return 1;
    }
    if(b%5 == 0){
        printf("Fizz \n");
        return 1;
    }
    return 0;
}

int primeCheck(int b){
///////////////////////////////////////////////////////////////////////
// Purpose:   Checks if the number is prime
// Input:     b
// Returns:   True(1) if input is prime. False(0) otherwise.
// Notes:     prints ...
// ... "BuzzFizz" when b is prime.
///////////////////////////////////////////////////////////////////////
    int c;

   for ( c = 2 ; c <= b ; c++ ){
        if ( b%c == 0 )
        return 0;
   }
   printf("BuzzFizz \n");
   return 1;
}