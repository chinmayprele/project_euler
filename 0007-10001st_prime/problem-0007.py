from tqdm import tqdm as tqdm

def is_prime(n):
	import math

	if (n < 2) or (n % 2 == 0 and n > 2):
		return( False )
	elif n == 2:
		return( True )
	elif n == 3:
		return( True )
	else:
		for i in range( 3, math.ceil(math.sqrt(n)) + 1, 2 ):
			if n % i == 0:
				return( False )
		return( True )


nth_prime = 10001
all_primes = []

current_num = 1
while len( all_primes ) <= nth_prime-1:
	if is_prime( current_num ):
		all_primes.append( current_num )
	current_num += 1

print( all_primes[-1] )
