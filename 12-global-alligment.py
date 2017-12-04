# 12-global-alligment

# input data
f = open('input12.txt')

v = f.readline()
w = f.readline()

f.close()

n = len(v) - 1
m = len(w)

scoring = [ 
[ 4,  0, -2, -1, -2,  0, -2, -1, -1, -1, -1, -2, -1, -1, -1,  1,  0,  0, -3, -2],
[ 0,  9, -3, -4, -2, -3, -3, -1, -3, -1, -1, -3, -3, -3, -3, -1, -1, -1, -2, -2],
[-2, -3,  6,  2, -3, -1, -1, -3, -1, -4, -3,  1, -1,  0, -2,  0, -1, -3, -4, -3],
[-1, -4,  2,  5, -3, -2,  0, -3,  1, -3, -2,  0, -1,  2,  0,  0, -1, -2, -3, -2],
[-2, -2, -3, -3,  6, -3, -1,  0, -3,  0,  0, -3, -4, -3, -3, -2, -2, -1,  1,  3],
[ 0, -3, -1, -2, -3,  6, -2, -4, -2, -4, -3,  0, -2, -2, -2,  0, -2, -3, -2, -3],
[-2, -3, -1,  0, -1, -2,  8, -3, -1, -3, -2,  1, -2,  0,  0, -1, -2, -3, -2,  2],
[-1, -1, -3, -3,  0,  4, -3,  4, -3,  2,  1, -3, -3, -3, -3, -2, -1,  3, -3, -1],
[-1, -3, -1,  1, -3, -2, -1, -3,  5, -2, -1,  0, -1,  1,  2,  0, -1, -2, -3, -2],
[-1, -1, -4, -3,  0, -4, -3,  2, -2,  4,  2, -3, -3, -2, -2, -2, -1,  1, -2, -1],
[-1, -1, -3, -2,  0, -3, -2,  1, -1,  2,  5, -2, -2,  0, -1, -1, -1,  1, -1, -1],
[-2, -3,  1,  0, -3,  0,  1, -3,  0, -3, -2,  6, -2,  0,  0,  1,  0, -3, -4, -2],
[-1, -3, -1, -1, -4, -2, -2, -3, -1, -3, -2, -2,  7, -1, -2, -1, -1, -2, -4, -3],
[-1, -3,  0,  2, -3, -2,  0, -3,  1, -2,  0,  0, -1,  5,  1,  0, -1, -2, -2, -1],
[-1, -3, -2,  0, -3, -2,  0, -3,  2, -2, -1,  0, -2,  1,  5, -1, -1, -3, -3, -2],
[ 1, -1,  0,  0, -2,  0, -1, -2,  0, -2, -1,  1, -1,  0, -1,  4,  1, -2, -3, -2],
[ 0, -1, -1, -1, -2, -2, -2, -1, -1, -1, -1,  0, -1, -1, -1,  1,  5,  0, -2, -2],
[ 0, -1, -3, -2, -1, -3, -3,  3, -2,  1,  1, -3, -2, -2, -3, -2,  0,  4, -3, -1],
[-3, -2, -4, -3,  1, -2, -2, -3, -3, -2, -1, -4, -4, -2, -3, -3, -2, -3, 11,  2],
[-2, -2, -3, -2,  3, -3,  2, -1, -2, -1, -1, -2, -3, -1, -2, -2, -2, -1,  2,  7] ]

# A  C  D  E  F  G  H  I  K  L  M  N  P  Q  R  S  T  V  W  Y

def fromAcid(s):
	ans = -1

	if s == 'A':
		ans = 0
	elif s == 'C':
		ans = 1
	elif s == 'D':
		ans = 2
	elif s == 'E':
		ans = 3
	elif s == 'F':
		ans = 4
	elif s == 'G':
		ans = 5
	elif s == 'H':
		ans = 6
	elif s == 'I':
		ans = 7
	elif s == 'K':
		ans = 8
	elif s == 'L':
		ans = 9
	elif s == 'M':
		ans = 10
	elif s == 'N':
		ans = 11
	elif s == 'P':
		ans = 12
	elif s == 'Q':
		ans = 13
	elif s == 'R':
		ans = 14
	elif s == 'S':
		ans = 15
	elif s == 'T':
		ans = 16
	elif s == 'V':
		ans = 17
	elif s == 'W':
		ans = 18
	elif s == 'Y':
		ans = 19

	return ans

lack = 5
s = [[0 for i in range(m+1)] for t in range(n+1)]


for i in range(1,n+1):
	s[i][0] += s[i-1][0] - lack

for j in range(1, m+1):
	s[0][j] += s[0][j-1] - lack


b = [[0 for i in range(m+1)] for t in range(n+1)]
for i in range(1,n+1):
	b[i][0] = 1

for j in range(1, m+1):
	b[0][j] = 2


for i in range(1,n+1):
	for j in range(1, m+1):
		tv = fromAcid(v[i-1])
		tw = fromAcid(w[j-1])

		a = s[i-1][j] - lack
		d = s[i][j-1] - lack
		c = s[i-1][j-1] + scoring[tv][tw]

		if c >= d:
			if a >= c:
				s[i][j] = a
				b[i][j] = 1 # up
			else:
				s[i][j] = c
				b[i][j] = 0 # 
				
		else: # d > c
			if a >= d:
				s[i][j] = a
				b[i][j] = 1 # up
			else:
				s[i][j] = d
				b[i][j] = 2 # 
		
		#s[i][j] = max(s[i-1][j] - lack, s[i][j-1] - lack, s[i-1][j-1] + scoring[tv][tw] )
		#print(s[i][j], " = s")

# print("\n")		
# for i in range(0, n+1):
# 	print(s[i])
				
# print("\n")		
# for i in range(0, n+1):
# 	print(b[i])

q = s[n][m]
# print(q)

ans1 = ''
ans2 = ''

i = n
j = m

while (i > 0) & (j > 0):
	if b[i][j] == 0:
		ans1 += w[j-1]
		ans2 += v[i-1]
		i -= 1
		j -= 1
		
	else:
		if b[i][j] == 1:
			ans1 += '-' 
			ans2 += v[i-1]
			i -= 1
		else:
			ans1 += w[j-1] 
			ans2 += '-'
			j -= 1

if i == 0:
	while j != 0:
		ans1 += w[i]
		ans2 += '-'
		j -= 1

if j == 0:
	while i != 0:
		ans1 += '-'
		ans2 += v[j]
		i -= 1

res1 = ''
for y in reversed(ans1):
	res1 += y

res2 = ''
for y in reversed(ans2):
	res2 += y

f = open('output.txt', 'w')
f.write(str(q) + "\n")
f.write(str(res2)+ "\n")
f.write(str(res1))

f.close()