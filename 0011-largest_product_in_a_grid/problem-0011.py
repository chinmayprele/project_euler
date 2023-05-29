# === imports =================================================================
from tqdm import tqdm as tqdm
from pprint import pprint as pprint
import numpy
import sys

# === data =================================================================

grid = []

with open( "grid20.grid", "r" ) as infile:
	for line in infile:
		nums = [ int( num ) for num in line.strip().split() ]
		grid.append( nums )

# === identify all 4mers ======================================================

all_4mers = set()

# HORIZONTAL
for row in grid:
	for i in range( len(row)-3 ):
		horizontal_4mer = [
			row[i],
			row[i+1],
			row[i+2],
			row[i+3],
		]
		all_4mers.add( tuple(horizontal_4mer) )

# VERTICAL
vertical_4mers = set()
for i in range( 0, 17 ):
	for j in range( len( grid[i] ) ):
		vertical_4mers.add( tuple([
			grid[i][j],
			grid[i+1][j],
			grid[i+2][j],
			grid[i+3][j],
		]) )
	# break
all_4mers.update( vertical_4mers )

# RIGHT DIAGONAL
rdiag_4mers = set()
for i in range( 0, 17 ):
	for j in range( 0, 17 ):
		rdiag_4mers.add( tuple([
			grid[i][j],
			grid[i+1][j+1],
			grid[i+2][j+2],
			grid[i+3][j+3],
		]) )
all_4mers.update( rdiag_4mers )
print( "     Number of 4mers = {0}".format( len( all_4mers ) ) )

# LEFT DIAGONAL
ldiag_4mers = set()
for i in range( 0, 17, 1 ):
	for j in range( 19, 3, -1 ):
		ldiag_4mers.add( tuple([
		# ldiag_4mers.add( tuple([
			grid[i][j],
			grid[i+1][j-1],
			grid[i+2][j-2],
			grid[i+3][j-3],
		]) )
all_4mers.update( ldiag_4mers )

print( "     Number of 4mers = {0}".format( len( all_4mers ) ) )

# === find product ============================================================

max_prod = 0
for kmer4 in tqdm( list( all_4mers ), desc="Identifying Product", leave=False ):
	if numpy.prod( list( kmer4 ) ) > max_prod:
		max_prod = numpy.prod( list( kmer4 ) )

print( "Max Product of 4mers = {0}".format( max_prod ) )
