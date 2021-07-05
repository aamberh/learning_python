import random
sequence = ''
length = 30
for i in range(length):
	r = random.randint(1, 10)
	if r <= 3:
		sequence += 'A'
	if r > 3 and r <= 6:
		sequence += 'T'	
	#print('A', end='') or print('T', end='')
	if r > 6 and r <= 8:
		sequence += 'G' 
	if r > 8:
		sequence += 'C'
	#print('G', end='') or print('C', end='')

AT_count = 0	
for i in range(length):
	if sequence[i] == 'A': 
		AT_count += 1
	elif sequence[i] == 'T':
		AT_count += 1
		
AT_fraction = AT_count / (length)
print(length, AT_fraction, sequence)


 