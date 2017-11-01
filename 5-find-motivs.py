# 5-find-motivs

# функция, считающая Score
def Score(DNA):
	Length = len(DNA[0])

	A = [0] * (Length)
	C = [0] * (Length)
	G = [0] * (Length)
	T = [0] * (Length)

	for r in range(t):
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
def Concat_piece(piece_txt, set):
	tmp = []
	for h in range(t):
		tmp.append(piece_txt[h][set[h]:set[h]+l])

	#print(tmp)
	return tmp


# start programm
f = open('input.txt')

# input data
l = int(f.read(1))
f.read(1)

t = int(f.read(1))
f.read(1)

text = f.readlines()

f.close()

lenLine = len(text[0])

# set of start of motivs
s = []
for y in range(t):
	s.append(0)

# запись в файл
f = open('output.txt', 'w')

# возьмем за максимум
sample_t = Concat_piece(text, s)		
maxScore = Score(sample_t)
set_motivs = []

# вспомогательная рекурсивная функция 
def Recur(p):
	global maxScore
	global set_motivs
	for j in range(p):

		for u in range(lenLine-l-1):
			s[j] += 1
			sample_t = Concat_piece(text, s)
			tScore = Score(sample_t)

			if tScore > maxScore:
				maxScore = tScore
				set_motivs = sample_t				

			#f.write(str(s))
			#f.write('\n')
			Recur(j)
		s[j] = 0


for i in range(t):
	for k in range(lenLine-l-1):
		s[i] += 1
		#f.write(str(s))
		#f.write('\n')

		Recur(i)
		
	s[i] = 0		
	#f.write('\n')

#print(maxScore)
#print(set_motivs)

#f.write(str(set_motivs))

for count in range(t):
	f.write(str(set_motivs[count]) + '\n')

f.close()
