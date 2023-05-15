from tqdm import tqdm as tqdm
from pprint import pprint as pprint

def collatz_size( seed ):
	if seed == 1:
		return( 0 )
	elif seed % 2 == 0:
		return( 1 + collatz_size( seed/2 ) )
	elif seed % 2 != 0:
		return( 1 + collatz_size( 3*seed + 1 ) )

collatz_seq_dict = dict()

for seed in tqdm( range( 1, int( 1e6+1 ) ) ):
	size = collatz_size( seed )
	if size in collatz_seq_dict.keys():
		collatz_seq_dict[ size ].append( seed )
	elif size not in collatz_seq_dict.keys():
		collatz_seq_dict[ size ] = [ seed ]
	# break


sorted_list = list(collatz_seq_dict.keys())
sorted_list.sort()

pprint( collatz_seq_dict[ sorted_list[-1] ] )
