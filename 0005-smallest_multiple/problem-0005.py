from tqdm import tqdm as tqdm

def check_divisible( num, start, end ):
	for i in range( start, end+1 ):
		if num % i != 0:
			return( False )
	return( True )

number = None

for i in tqdm( range( 1, int( 1e10 ) ) ):
	if check_divisible( i, 1, 20 ) == True:
		number = i
		break

print( number )
