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
	#print("global ", i)
	if i < L-1:
		a[i+1] = 0
		i += 1
		#print(a, "level = ", i)
		return a
	else:
		for y in range(L):
			j = L - y - 1
			if a[j] < k:
				# if j < L-1:
				# 	a[j+1] = 0
				a[j] += 1
				i = j+1
				#print(a, "level = ", i)
				return a
			else:
				#a[j] = -1
				i = j - 1
	i = 0
	#print(a, "level =", i)
	return a

def NextVertex1(a, L, k):
	global i
	#print("global ", i)
	if i < L:
		i += 1
		return a
	else:
		for y in range(L):
			j = L - y - 1
			if a[j] < k:
				a[j] += 1
				#i = j
				return a
			else:
				a[j] = 0
				i -= 1
	i = 0
	return a




def Bypass(a, L, k):
	global i
	#print("i in bypass", i)
	for y in range(i):
		j = i - y
		if a[j] < k:
			a[j] += 1
			#i = j
			#print(a, "j = ", i)
			return a
		else:
			a[j] = 0
			if a[j-1] != k:
				a[j-1] += 1
				#i = j
				#print("ii", i)
				return a 
	i = 0
	#print(a, "j = ", i)
	return a

def Bypass1(a,L,k):
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
				if a[j-1] != k:
					a[j-1] += 1
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
f = open('in6.txt')

#input data
l = int(f.readline()) # 3
print("l=",l)
text = f.readlines()

t = len(text)
lenLine = len(text[0])
K = 3
bestWord = ''
bestDistance = (t+1) * l + 1
print("bestDi = ",bestDistance)

s = [0 for q in range(l)]

# i = 3
# for h in range(20): #((K+1)**(l+1)):
# 	g = Bypass1(s, l, K)
# 	print(g, " ", i)


i = 1
while i > 0:
	if i < l:
		prefix = inDNA(s[0:i])
		#print(prefix , " pr i ", i)
		optimisticDistance = TotalDistance(prefix, text)
		#print(optimisticDistance)
		if optimisticDistance > bestDistance:
			s = Bypass1(s, l, K)
			#print(i, "bypass i")
		else:
			s = NextVertex1(s, l, K)
			#print(i, "NextVertex i")
	else:
		#print("ss", s)
		word = inDNA(s)
		t_total = TotalDistance(word,text)
		#print("t_total",t_total)
		if t_total < bestDistance:
			bestDistance = t_total
			#print("bestDistance", bestDistance)
			bestWord = word
			#print("current best = ", bestWord)
		s = NextVertex1(s, l, K)
		#print("NextVertex")

print("print", bestWord)

# write in file
#f = open('output.txt', 'w')
#f.write(bestWord)

#f.close()