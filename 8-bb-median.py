# 8-branch-and-bound-median

#   Hint:
#   L = l, a = l-mer, k = 3 - 0,1,2,3 - letter in DNA

def NextLeaf(a,L,k):
	for i in range(L):
		j = L - i - 1
		if a[j] < k:
			a[j] += 1
			return a
		a[j] = 0
	return a

def AllLeaves(L,k):
	a = [0 for i in range(L)]
	print((k+1) ** L)
	for i in range((k+1) ** L):
		#print(a)
		a = NextLeaf(a, L, k)

def NextVertex(a, L, k):
	global i
	if i < L:
		i += 1
		return a
	else:
		for y in range(L):
			j = L - y - 1
			if a[j] < k:
				a[j] += 1
				return a
			else:
				a[j] = 0
				i -= 1
	i = 0
	return a

def Bypass(a,L,k):
	global i
	if i != 0:
		for y in range(i):
			j = i - y - 1 #+1
			if a[j] < k:
				a[j] += 1
				return a
			else:
				i -= 1
				a[j] = 0
				# if a[j-1] != k:
				# 	a[j-1] += 1
				# 	return a
				for p in range(j):
					b = j - p - 1
					if a[b] != k:
						a[b] += 1
						return a
					else:
						a[b] = 0
				i = 0
				return a
		i = 0
		return a
	else:
		return a

def inDNA(w):
	response = ''
	for i in range(len(w)):
		if w[i] == 0:
			response += 'A'
		elif w[i] == 1:
			response += 'C'
		elif w[i] == 2:
			response += 'G'
		elif w[i] == 3:
			response += 'T'
	return response

def dH(first, second):
	count = 0
	for i in range(len(first)):
		if first[i] != second[i]:
			count += 1
	return count

def mindH(sample, line):
	tmp_min = l
	for u in range(lenLine - l): # -1
		tmp_dH = dH(sample, line[u:u+l])
		if tmp_dH < tmp_min:
			tmp_min = tmp_dH
	return tmp_min

def TotalDistance(v, _text):
	tmp_count = 0
	for j in range(t):
		tmp_count += mindH(v, _text[j])
	return tmp_count

# start a programm
f = open('input.txt')

#input data
l = int(f.readline())

text = f.readlines()

t = len(text)
lenLine = len(text[0])

K = 3
bestWord = ''
bestDistance = (t+1) * l + 1

s = [0 for q in range(l)]

i = 1
while i > 0:
	if i < l:
		prefix = inDNA(s[0:i])
		optimisticDistance = TotalDistance(prefix, text)
		if optimisticDistance > bestDistance:
			s = Bypass(s, l, K)
		else:
			s = NextVertex(s, l, K)
	else:
		word = inDNA(s)
		t_total = TotalDistance(word,text)
		if t_total < bestDistance:
			bestDistance = t_total
			bestWord = word
		s = NextVertex(s, l, K)

#print("print", bestWord)

# write in file
f = open('output.txt', 'w')
f.write(bestWord)

f.close()