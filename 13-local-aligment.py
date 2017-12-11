# 13-local-aligment

# input data
f = open('input.txt')

v = f.readline()
w = f.readline()

f.close()

n = len(v) - 1
m = len(w)

scoring = [ 
[  2, -2,  0,  0, -3,  1, -1, -1, -1, -2, -1,  0,  1,  0, -2,  1,  1,  0, -6, -3],
[ -2, 12, -5, -5, -4, -3, -3, -2, -5, -6, -5, -4, -3, -5, -4,  0, -2, -2, -8,  0],
[  0, -5,  4,  3, -6,  1,  1, -2,  0, -4, -3,  2, -1,  2, -1,  0,  0, -2, -7, -4],
[  0, -5,  3,  4, -5,  0,  1, -2,  0, -3, -2,  1, -1,  2, -1,  0,  0, -2, -7, -4],
[ -3, -4, -6, -5,  9, -5, -2,  1, -5,  2,  0, -3, -5, -5, -4, -3, -3, -1,  0,  7],
[  1, -3,  1,  0, -5,  5, -2, -3, -2, -4, -3,  0,  0, -1, -3,  1,  0, -1, -7, -5],
[ -1, -3,  1,  1, -2, -2,  6, -2,  0, -2, -2,  2,  0,  3,  2, -1, -1, -2, -3,  0],
[ -1, -2, -2, -2,  1, -3, -2,  5, -2,  2,  2, -2, -2, -2, -2, -1,  0,  4, -5, -1],
[ -1, -5,  0,  0, -5, -2,  0, -2,  5, -3,  0,  1, -1,  1,  3,  0,  0, -2, -3, -4],
[ -2, -6, -4, -3,  2, -4, -2,  2, -3,  6,  4, -3, -3, -2, -3, -3, -2,  2, -2, -1],
[ -1, -5, -3, -2,  0, -3, -2,  2,  0,  4,  6, -2, -2, -1,  0, -2, -1,  2, -4, -2],
[  0, -4,  2,  1, -3,  0,  2, -2,  1, -3, -2,  2,  0,  1,  0,  1,  0, -2, -4, -2],
[  1, -3, -1, -1, -5,  0,  0, -2, -1, -3, -2,  0,  6,  0,  0,  1,  0, -1, -6, -5],
[  0, -5,  2,  2, -5, -1,  3, -2,  1, -2, -1,  1,  0,  4,  1, -1, -1, -2, -5, -4],
[ -2, -4, -1, -1, -4, -3,  2, -2,  3, -3,  0,  0,  0,  1,  6,  0, -1, -2,  2, -4],
[  1,  0,  0,  0, -3,  1, -1, -1,  0, -3, -2,  1,  1, -1,  0,  2,  1, -1, -2, -3],
[  1, -2,  0,  0, -3,  0, -1,  0,  0, -2, -1,  0,  0, -1, -1,  1,  3,  0, -5, -3],
[  0, -2, -2, -2, -1, -1, -2,  4, -2,  2,  2, -2, -1, -2, -2, -1,  0,  4, -6, -2],
[ -6, -8, -7, -7,  0, -7, -3, -5, -3, -2, -4, -4, -6, -5,  2, -2, -5, -6, 17,  0],
[ -3,  0, -4, -4,  7, -5,  0, -1, -4, -1, -2, -2, -5, -4, -4, -3, -3, -2,  0, 10] ]

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
	
	
s = [[0 for i in range(m+1)] for t in range(n+1)]
#print(s)

b = [[0 for i in range(m+1)] for t in range(n+1)]
#print(b)

lack = 5

for i in range(1,n+1):
	s[i][0] += s[i-1][0] - lack
	b[i][0] = 1

for j in range(1, m+1):
	s[0][j] += s[0][j-1] - lack
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
				if (0 >= a):
					s[i][j] = 0
					b[i][j] = 3 # jump
				else:
					s[i][j] = a
					b[i][j] = 1 # up
			else:
				if (0 >= c):
					s[i][j] = 0
					b[i][j] = 3 # jump
				else:
					s[i][j] = c
					b[i][j] = 0 # 
				
		else: # d > c
			if a >= d:
				if (0 >= a):
					s[i][j] = 0
					b[i][j] = 3 # jump
				else:
					s[i][j] = a
					b[i][j] = 1 # up
			else: # d > a
				if (0 >= d):
					s[i][j] = 0
					b[i][j] = 3 # jump
				else:
					s[i][j] = d
					b[i][j] = 2 # 

# print("\n")		
# for i in range(0, n+1):
# 	print(s[i])
				
# print("\n")		
# for i in range(0, n+1):
# 	print(b[i])

i_max = 0
j_max = 0
s_max = s[0][0]

for i in range(1,n+1):
	for j in range(1,m+1):
		if s[i][j] >= s_max:
			s_max = s[i][j]
			i_max = i
			j_max = j

# print("s_max", s_max,"i_max", i_max, "j_max", j_max)

ans1 = ''
ans2 = ''

i = i_max
j = j_max

while (b[i][j] != 3 ) & (i > 0) & (j > 0):
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

res1 = ''
for y in reversed(ans1):
	res1 += y

res2 = ''
for y in reversed(ans2):
	res2 += y

f = open('output.txt', 'w')
f.write(str(s_max) + "\n")
f.write(str(res2)+ "\n")
f.write(str(res1))

f.close()