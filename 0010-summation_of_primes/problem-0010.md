# [Summation of primes](https://projecteuler.net/problem=10) 

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

## Answers 

1. &larr;

## Notes

- As the numbers during the iteration increase, the `is_prime()` function is taking longer and longer to run.
	- A solution would have been to multithread each of these numbers to run on individual cores so that many numbers can be computed as primes at once.
	- An alternate solution would also be to identiefy from online the list of primes from a database, but that isn't fun.
