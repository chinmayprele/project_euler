# [Summation of primes](https://projecteuler.net/problem=10) 

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

## Answers 

1. `142913828923` &larr; Incorrect
	- Did not account for _1_
2. `142913828922` &larr; Correct

## Notes

- As the numbers during the iteration increase, the `is_prime()` function is taking longer and longer to run.
	- A solution would have been to multithread each of these numbers to run on individual cores so that many numbers can be computed as primes at once.
	- An alternate solution would also be to identiefy from online the list of primes from a database, but that isn't fun.

Though it was possible to multithread the output, I intentified the following issues:

- The following function was too slow since it went through too many iterations.
	```Python
	def is_prime( number ):
		for i in range( 2, number ):
			if number % i == 0:
				return( False )
		if number <= 1:
			return( False )
		return( True )
	```
- Instead, the following function was much quicker since it:
	1. Only went upto the square root of the number,
	2. Skipped checking multiples of _2_, and 
	3. Checked for evenness early on during validation.
	```Python
	def is_prime(n):
		if (n < 2) or (n % 2 == 0 and n > 2):
			return False
		elif n == 2:
			return True
		elif n == 3:
			return True
		else:
			for i in range(3, math.ceil(math.sqrt(n)) + 1, 2):
				if n % i == 0:
					return False
			return True
	```
