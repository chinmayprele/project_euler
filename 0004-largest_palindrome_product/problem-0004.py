from tqdm import tqdm as tqdm
import sys

def is_palindrome( num ):

	if str( num ) == str( num )[::-1]:
		return( True )
	else:
		return( False )


palindrome = None

for i in range( 999, 1, -1 ):
	found = False
	for j in range( 999, 1, -1 ):
		if is_palindrome( i*j ):
			print( i )
			print( j )
			print( i*j )
			found = True
		break
	if found:
		break


