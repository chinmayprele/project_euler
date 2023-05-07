fib0 = 0
fib1 = 1

fib_even_set = set()

for i in range( 100000 ):
	fib_sum = fib0 + fib1
	if fib_sum >= 4e6:
		break
	if fib_sum%2 == 0:
		fib_even_set.add( fib_sum )
	fib0 = fib1
	fib1 = fib_sum

print( sum(fib_even_set) )
