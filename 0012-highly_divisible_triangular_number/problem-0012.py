from tqdm import tqdm as tqdm
from pprint import pprint as pprint
from tqdm import trange

def triangle_number( cardinality ):
	nums = [ num for num in range( 1, cardinality+1 ) ]
	return( sum( nums ) )

def factorizer_optimized( number, factor_dict ):
	"""
	Returns the number of factors that a number has as a set
	"""
	import math

	out_set = set()
	for i in range( math.floor(number), 0, -1 ):
		if number % i == 0:
			out_set.add( i )
			if i in factor_dict.keys():
				out_set.update( factor_dict[i] )
				break
	factor_dict[ number ] = out_set
	return( out_set )

def factorizer( number ):
	out_set = set()
	for i in range( number, 0, -1 ):
		if number % i == 0:
			out_set.add( i )
	return( out_set )

def optimal_factors( x ):
	result = []
	i = 1
	while i*i <= x:
		if x % i == 0:
			result.append(i)
			if x//i != i: # In Python, // operator performs integer/floored division
				result.append(x//i)
		i += 1
	# Return the list of factors of x
	return( result )


min_factors = 500
range_to_search = int(1e5)

factor_dict = dict()

loop_range = trange( int(1e5), desc="Identifying Factors for Triangle Numbers", leave=True )

for cardinality in loop_range:
	# n_factors = len( factorizer( triangle_number( cardinality ) ) )
	# n_factors = len( factorizer_optimized( triangle_number( cardinality ), factor_dict ) )
	n_factors = len( optimal_factors( triangle_number( cardinality ) ) )
	loop_range.set_description( "Identifying Factors for Triangle Numbers {0:>5}".format( n_factors ) )
	if n_factors > min_factors:
		# pprint( factor_dict )
		print( "The {0}th triangle number {1} has {2} factors.".format( cardinality, triangle_number( cardinality ), n_factors ) ) 
		break
