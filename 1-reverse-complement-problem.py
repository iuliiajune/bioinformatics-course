# 1-reverse-complement-problem
f = open('input.txt')

Pattern = f.read()
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

print(InvPattern)
f.close

f = open('output.txt', 'w')
f.write(str(InvPattern))

f.close()