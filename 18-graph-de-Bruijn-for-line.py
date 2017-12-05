# 18-graph-de-Bruijn-for-line

# input data
f = open('input16.txt')

k = int(f.readline())
v = str(f.readline())

p = len(v)

pattern = []
for i in range(p-k+1):
	t = v[i:i+k]
	pattern.append(t)

f.close()

# print(pattern)

n = len(pattern)

v = []
v.append(pattern[0][0:k-1])
v.append(pattern[0][1:k])

lenV = 2

def addV(length, w):
	global v
	global i
	j = 0
	while j < length:
		if (v[j] == w):
			return 0
		j += 1
	v.append(w)
	return 1

for i in range(1,n):
	# print("lenV = ", lenV, " len = ", len(v))
	lenV += addV(lenV, pattern[i][0:k-1])
	lenV += addV(lenV, pattern[i][1:k])

# print(v)

m = len(v)
s = [[0 for i in range(m)] for j in range(m)]

t = ''
for i in range(n):
	for j in range(m):
		if pattern[i][0:k-1] == v[j]:
			for y in range(m):
				if pattern[i][1:k] == v[y]:
					s[j][y] += 1

# print("\n")		
# for i in range(0, m):
# 	print(s[i])

f = open('output.txt', 'w')
f = open('output.txt', 'a')

t = ''
flag = 0

for j in range(m):
	flag = 0
	t = v[j] + " -> "
	for y in range(m):
		if (s[j][y] != 0):
			for u in range(s[j][y]):
				if (flag == 0):
					t += v[y]
					flag +=1 
				else:	
					t += "," + v[y]
	f.write(t + "\n")
	# print(t)			

f.close()