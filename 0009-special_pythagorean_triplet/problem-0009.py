from tqdm import tqdm as tqdm
import math
from pprint import pprint as pprint
import numpy

def is_square( number ):
	import math
	if int( math.sqrt( number ) + 0.5) ** 2 == number:
		return( True )
	else:
		return( False )


triplets = []

for b in range( 100, 500 ): # find b
	for a in range( 1, b ): # find a
		c_square = a*a + b*b
		if is_square( c_square ):
			triplets.append([ a, b, int( math.sqrt( c_square ) ) ])

for triplet in triplets:
	if triplet[0] + triplet[1] + triplet[2] == 1000:
		print( triplet )
		print( numpy.prod( triplet ) )
