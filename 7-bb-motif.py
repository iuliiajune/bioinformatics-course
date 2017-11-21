# 7-branch-and-bound-motif

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
			j = i - y - 1 
			if a[j] < k:
				a[j] += 1
				return a
			else:
				i -= 1
				a[j] = 0
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

# функция, считающая Score
def Score(DNA):
	global i
	Length = len(DNA[0])

	A = [0] * (Length)
	C = [0] * (Length)
	G = [0] * (Length)
	T = [0] * (Length)

	for r in range(i):
		for m in range(Length):
			z = DNA[r][m]
			if z == 'A':
				A[m] += 1
			elif z == 'C':
				C[m] += 1
			elif z == 'G':
				G[m] += 1
			elif z == 'T':
				T[m] += 1

	#print(A), print(C), print(G), print(T)

	score = 0
	for b in range(Length):
		maxCount = max(A[b], C[b], G[b], T[b])
		score += maxCount

	#print(score)
	return score

# функция, склеивающая куски для мотивов 
def Concat_piece(piece_txt, set, i):
	tmp = []
	for h in range(i):
		tmp.append(piece_txt[h][set[h]:set[h]+l])
	return tmp

# start a programm
f = open('input.txt')

#input data
l = int(f.read(1))
f.read(1)
t = int(f.read(1))
f.read(1)
text = f.readlines()
f.close()

n = len(text[0]) - 1

s = [0 for q in range(t)]

bestScore = 0
bestS = []
bestMotifs = []

K = n - l
i = 1
#f = open('help.txt', 'w')
while i > 0:
	# f.write("i for"+ str(i) + '\n')	
	if i < t:
		DNA = Concat_piece(text, s, i);
		# f.write("DNA"+str(DNA) + '\n')
		sco = Score(DNA)
		optimisticScore = sco + (t - i) * l
		# f.write("optimisticScore"+str(optimisticScore)+ "bestScore"+ str(bestScore) + '\n')
		if optimisticScore < bestScore:
			s = Bypass(s, t, K)
			# f.write("s by"+ str(s) + '\n')
		else:
			s = NextVertex(s, t, K)
			# f.write("s ne1"+ str(s) + '\n')
	else:
		DNA = Concat_piece(text, s, i);
		# f.write("DNA"+ str(DNA) + '\n')
		t_score = Score(DNA)
		# f.write("t_score"+str(t_score)+ "bestScore"+ str(bestScore) + '\n')
		if t_score >= bestScore:
			bestScore = t_score
			# f.write("\t\t\t\t bestScore"+str(bestScore) + '\n')
			bestS = s
			bestMotifs = Concat_piece(text, bestS, t)
		s = NextVertex(s, t, K)
		# f.write("s ne2"+ str(s) + '\n')
	

# for count in range(t):
# 	print(bestMotifs[count])

# write in file
f = open('output.txt', 'w')
for count in range(t):
	f.write(str(bestMotifs[count]) + '\n')

f.close()