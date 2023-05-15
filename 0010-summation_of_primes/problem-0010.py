from tqdm import tqdm as tqdm

def is_prime( number ):
	for i in range( 2, number ):
		if number % i == 0:
			return( False )
	return( True )

rolling_sum = 0

for i in tqdm( range( 1, int(2e6)+1 ) ):
	if is_prime( i ):
		rolling_sum += i

print( rolling_sum )
