# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places
# Use all three formatting methods
0.42
0.42
0.42

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT'
GC = 0
for total in range(0, len(dna)):
	total += 1
for i in range(0, len(dna)):
	if dna[i] == 'C': 
		GC += 1
	elif dna[i] == 'G':
		GC += 1
portion = GC / total
print(f'{portion:.2f}')
print('{:.2f}'.format(portion))
print('%.2f' % (portion))

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT'
GC = 0
for i in range(0, len(dna)):
	if dna[i] == 'C': 
		GC += 1
	elif dna[i] == 'G':
		GC += 1
portion = GC / (len(dna))
print(f'{portion:.2f}')
print('{:.2f}'.format(portion))
print('%.2f' % (portion))





