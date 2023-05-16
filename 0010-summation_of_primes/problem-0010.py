from tqdm import tqdm as tqdm
import time
import math
from multiprocessing import Pool
from multiprocessing import freeze_support
import sys


# def run_multiprocessing(func, i, n_processors):
# 	'''
# 	Define function to run mutiple processors and pool the results together
# 	'''
# 	with Pool(processes=n_processors) as pool:
# 		return pool.map(func, i)

# def is_prime( number ):
# 	for i in range( 2, number ):
# 		if number % i == 0:
# 			return( False )
# 	if number <= 1:
# 		return( False )
# 	return( True )

def is_prime(n):
	if (n < 2) or (n % 2 == 0 and n > 2):
		return False
	elif n == 2:
		return True
	elif n == 3:
		return True
	else:
		for i in range(3, math.ceil(math.sqrt(n)) + 1, 2):
			if n % i == 0:
				return False
		return True

rolling_sum = 0

for i in tqdm( range( 2, int(2e6)+1 ) ):
	if is_prime( i ):
		rolling_sum += i

print( rolling_sum )

sys.exit( "only needed to change function; following multothreading works" )

# def main():
# 	start = time.perf_counter()

# 	'''
# 	set up parameters required by the task
# 	'''
# 	num_max = int(2e6)+1
# 	n_processors = 6
# 	x_ls = list(range(1, num_max))

# 	'''
# 	pass the task function, followed by the parameters to processors
# 	'''
# 	out = run_multiprocessing(is_prime, x_ls, n_processors)

# 	print("Input length: {}".format(len(x_ls)))
# 	print("Output length: {}".format(len(out)))
# 	print("Mutiprocessing time: {}mins\n".format((time.perf_counter()-start)/60))
# 	print("Mutiprocessing time: {}secs\n".format((time.perf_counter()-start)))


# if __name__ == "__main__":
# 	freeze_support()   # required to use multiprocessing
# 	main()

# prime_mutiprocessing.py

import time
import math
from multiprocessing import Pool
from multiprocessing import freeze_support


'''Define function to run mutiple processors and pool the results together'''
def run_multiprocessing(func, i, n_processors):
	with Pool(processes=n_processors) as pool:
		return pool.map(func, i)

'''Define task function'''
def is_prime(n):
	if (n < 2) or (n % 2 == 0 and n > 2):
		return False
	elif n == 2:
		return True
	elif n == 3:
		return True
	else:
		for i in range(3, math.ceil(math.sqrt(n)) + 1, 2):
			if n % i == 0:
				return False
		return True

# def is_prime( number ):
# 	'''
# 	This function is TOO SLOW.
# 	'''
# 	for i in range( 2, number ):
# 		if number % i == 0:
# 			return( False )
# 	if number <= 1:
# 		return( False )
# 	return( True )

def find_indices( list_to_check, item_to_find ):
	indices = []
	for idx, value in enumerate(list_to_check):
		if value == item_to_find:
			indices.append( idx + 1 )
	return indices

def main():
	start = time.perf_counter()

	'''
	set up parameters required by the task
	'''
	num_max = int( 2e6 + 1 )
	n_processors = 6
	x_ls = list(range(1, num_max))

	'''
	pass the task function, followed by the parameters to processors
	'''
	prime_bool = run_multiprocessing(is_prime, x_ls, n_processors)

	print("Input length: {}".format(len(x_ls)))
	print("Output length: {}".format(len(prime_bool)))
	print("Mutiprocessing time: {}mins\n".format((time.perf_counter()-start)/60))
	print("Mutiprocessing time: {}secs\n".format((time.perf_counter()-start)))

	nums = find_indices( prime_bool, True )

	print( nums[:5] )


if __name__ == "__main__":
	freeze_support()   # required to use multiprocessing
	main()



