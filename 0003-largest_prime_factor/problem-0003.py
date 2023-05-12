import math

def is_prime(n):
	if n < 2:
		return False
	i = 2
	while i*i <= n:
		if n % i == 0:
			return( False )
		i += 1
	return( True )

num = 600851475143

prime_set = set()

for i in range( 2, math.floor( math.sqrt( num ) ) ):
	if num % i == 0 and is_prime( i ):
		prime_set.add( i )

print( sorted( prime_set ) )
