# 6-median-string-problem

# start a programm
f = open('input.txt')

# input data
l = int(f.readline())

text = f.readlines()
t = len(text)

lenLine = len(text[0])

f.close()

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

def inDNA(w):
	response = ''
	for i in range(l):
		if w[i] == 0:
			response += 'A'
		elif w[i] == 1:
			response += 'C'
		elif w[i] == 2:
			response += 'G'
		elif w[i] == 3:
			response += 'T'
	return response

# start a counting
bestWord = ''
bestDistance = (t+1) * l + 1
t_total_dist = 0

# set of start of words
word = [0 for q in range(l)]

word[0] = -1

countSymbol = 4 # count of Symbol in DNA

#f = open('words.txt', 'w')

# вспомогательная рекурсивная функция 
def Recur(p):
	global bestDistance
	global bestWord
	global t_total_dist
	for j in range(p):
		for u in range(countSymbol-1):
			word[j] += 1

			wordDNA = inDNA(word)
			#print(wordDNA)

			t_total_dist = TotalDistance(wordDNA, text)
			#print("total ", t_total_dist)

			if t_total_dist < bestDistance:
				bestDistance = t_total_dist
				bestWord = wordDNA
				#print(bestWord)

			#f.write(str(word))
			#f.write('\n')
			
			Recur(j)
		word[j] = 0

for i in range(l):
	for k in range(countSymbol-1):
		word[i] += 1
		#f.write(str(word))
		#f.write('\n')
		wordDNA = inDNA(word)
		#print(wordDNA)

		t_total_dist = TotalDistance(wordDNA, text)
		#print("total ", t_total_dist)

		if t_total_dist < bestDistance:
			bestDistance = t_total_dist
			bestWord = wordDNA
			#print(bestWord)

		Recur(i)

	word[i] = 0		
	#f.write('\n')

# write in file
f = open('output.txt', 'w')
f.write(bestWord)

f.close()