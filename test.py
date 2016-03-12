'''
# Problem Statement


# Software, Product, and Embedded Engineering Candidates

In the programming language of your choice, write a program
generating the first n Fibonacci numbers F(n), printing ...
- ... "Buzz" when F(n) is divisible by 3.
- ... "Fizz" when F(n) is divisible by 5.
- ... "BuzzFizz" when F(n) is prime.
- ... the value F(n) otherwise.

Bonus points for efficient implementation, testing, documentation,
and/or upload your code to GitHub.
'''

'''
///////////////////////////////////////////////////////////////////////
// Filename: test.py
//
// Synopsis: Main program file for demonstration code
//
// Purpose:
// Write a program generating the first n Fibonacci numbers f(n), printing ...
// ... "Buzz" when f(n) is divisible by 3.
// ... "Fizz" when f(n) is divisible by 5.
// ... "BuzzFizz" when f(n) is prime.
// ... the value f(n) otherwise.
//
///////////////////////////////////////////////////////////////////////
'''
# Divide operation(by 3 and by 5)


def divBy_op(b):
    if ((b % 3) == 0):
        print "Buzz"
        return True
    if ((b % 5) == 0):
        print "Fizz"
        return True


# To check if the number is prime
def primeCheck(b):
    if b > 1:
        for i in range(2, b):
            if (b % i) == 0:
                break
        else:
            print "BuzzFizz"
            return True
'''
///////////////////////////////////////////////////////////////////////
// Purpose:    Generates Fibonacci Sequence
// Input:      n
// Returns:    Nothing / void
// Calls:      divBy_op(), primeCheck();
///////////////////////////////////////////////////////////////////////
'''


def fibo(n):
    a = 0
    b = 1
#    print b
    for x in range(0, n):
        t = a
        a = b
        b += t
#       function calls to  prime number checking and divide by operation
        if divBy_op(b) == True or primeCheck(b) == True:
            continue
#       If none of the above conditions are True print the fibonacci number
        else:
            print b

totalNumber = int(raw_input("Enter the number of Fibonacci numbers required:"))
if totalNumber < 2:
    print "please input a number greater than 2"
else:
    print ("required fibonacci series:")
    fibo(totalNumber)
