'''
# Software, Product, and Embedded Engineering Candidates

In the programming language of your choice, write a program
generating the first n Fibonacci numbers F(n), printing ...
- ... "Buzz" when F(n) is divisible by 3.
- ... "Fizz" when F(n) is divisible by 5.
- ... "BuzzFizz" when F(n) is prime.
- ... the value F(n) otherwise.

Bonus points for efficient implementation, testing, documentation,
and/or upload your code to GitHub.

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
// ... first checks for the prime numbers
// ... then checks for divisibality by 3 and 5
// ... program only prints one of conditions in the order of occurance
// ... prime number check, divisibality by 5 or divisibality by 3
///////////////////////////////////////////////////////////////////////
'''

# Divide by 3 operation


def divBy_op(b):
    flag = False
    if ((b % 5) == 0):
        print str(b) + " :Fizz"
        flag = True
    elif (flag is False) and ((b % 3) == 0):
        print str(b) + " :Buzz"
        flag = True
    return flag


# Divide by 5 operation
'''def divBy_5(b):
    if ((b % 5) == 0):
        print "Fizz"
        return True
'''

# To check if the number is prime


def primeCheck(b):
    if b > 1:
        for i in range(2, b):
            if (b % i) == 0:
                break
        else:
            print str(b) + " :BuzzFizz"
            return True
'''
///////////////////////////////////////////////////////////////////////
// Purpose:    Generates Fibonacci Sequence
// Input:      n
// Returns:    Nothing / void
// Calls:      divBy_op(), primeCheck();
// Notes:      printing the value f(n) when not prime or divisible be 3 or 5.
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
#       Checking is the number is divisible by 3 or 5 or if it is a prime number
        if primeCheck(b) == True:
            continue
        elif divBy_op(b) == True:
            continue
#       If none of the above conditions are True print the fibonacci number
        else:
            print b

totalNumber = int(raw_input("Enter the number of Fibonacci numbers required:"))
if totalNumber < 2:
    print "please input required fibanacci numbers greater than 2"
else:
    print ("required fibonacci series is :")
    fibo(totalNumber)
    
