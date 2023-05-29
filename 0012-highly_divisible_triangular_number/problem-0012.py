from tqdm import tqdm as tqdm
from pprint import pprint as pprint

def triangle_number( cardinality ):
	nums = [ num for num in range( 1, cardinality+1 ) ]
	return( sum( nums ) )

def factorizer_optimized( number, factor_dict ):
	"""
	Returns the number of factors that a number has as a set
	"""
	out_set = set()
	for i in range( number, 0, -1 ):
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


min_factors = 500
range_to_search = int(1e5)

factor_dict = dict()

for cardinality in tqdm( range( range_to_search ), desc="Identifying Factors for Triangle Numbers" ):
	# n_factors = len( factorizer( triangle_number( cardinality ) ) )
	n_factors = len( factorizer_optimized( triangle_number( cardinality ), factor_dict ) )
	if n_factors > min_factors:
		# pprint( factor_dict )
		print( "The {0}th triangle number {1} has {2} factors.".format( cardinality, triangle_number( cardinality ), n_factors ) ) 
		break
