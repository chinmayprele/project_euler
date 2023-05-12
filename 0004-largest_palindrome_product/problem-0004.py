from tqdm import tqdm as tqdm
import sys

def is_palindrome( num ):

	if str( num ) == str( num )[::-1]:
		return( True )
	else:
		return( False )


palindrome = None
palindrome_set = set()

for i in range( 999, 100, -1 ):
	for j in range( 999, 100, -1 ):
		if is_palindrome( i*j ):
			palindrome_set.add( i*j )

print( max(palindrome_set) )
