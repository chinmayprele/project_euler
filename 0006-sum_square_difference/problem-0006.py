rolling_sq_sum = 0
rolling_sum = 0

for i in range( 1, 101 ):
	rolling_sq_sum += i*i
	rolling_sum += i

print( rolling_sum*rolling_sum - rolling_sq_sum )
