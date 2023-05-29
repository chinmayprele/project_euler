# === imports =================================================================
from tqdm import tqdm as tqdm
from pprint import pprint as pprint
from num2words import num2words

# === code =================================================================

start_num = 1
end_num = 1000

total_size = 0

for num in range( start_num, end_num+1 ):
	total_size += len( num2words(num, to="cardinal").replace( " ", "" ).replace( "-", "" ) )

print( total_size )
