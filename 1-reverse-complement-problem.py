#print('Enter string:')

# variable 'flag' allow to avoid a wrong input string
flag = 1

while flag == 1:
	flag = 0
	Pattern = str(input())
	InvPattern = ''
	for s in Pattern[::-1]:
		if s == 'A':
			InvPattern += 'T'
		elif s == 'C':
			InvPattern += 'G'
		elif s == 'G':
			InvPattern += 'C'
		elif s == 'T':
			InvPattern += 'A'
		else:
			print('Input string should be a part DNA and consist olny "A", "C", "G", "T" letters')
			print('Try again:')
			flag = 1
			break

#print('Output:')
print(InvPattern)