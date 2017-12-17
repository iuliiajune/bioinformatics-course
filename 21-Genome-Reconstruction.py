# 21-Genome-Reconstruction

# input data
f = open('input.txt')
k = int(f.readline())
data = f.readlines()
f.close()

# print(k)
n = len(data)

pattern = []
for i in range(n):
	pattern.append(str(data[i][0:k]))

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
# print("v",v)

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
	
_j = 0
_i = 0
for i in range(m):
	s_str = sum(s[i])
	s_stl = 0
	for j in range(m):
		s_stl += s[j][i]
	# print(s_str, " - ", s_stl)

	if s_str > s_stl:
		_j = i
	if s_stl > s_str:
		_i = i

s[_i][_j] = 1

# print("\n")		
# for i in range(0, m):
# 	print(s[i])
	
edge = n
i = 0
j = 0
c = 0
ver = []
flag = -1
matr_flag = -1
while c < edge+1:
	matr_flag = -1

	while j < n+1:
		if s[i][j] == 1:
			matr_flag += 1
			if matr_flag == 0:
				flag += 1
				ver.append([])

				y = 0
				while y < len(ver[flag-1]):
					# print(ver[flag-1][y])
					# print("i", i)

					if ver[flag-1][y] == i: #d[i][0]:
						t_count = 0
						p = y
						while p < len(ver[flag-1]):
							ver[flag].append(ver[flag-1][p])
							p += 1
							t_count += 1
						if t_count < len(ver[flag-1]):
							u = 0
							while (u < y):
								ver[flag].append(ver[flag-1][u])
								u += 1
					y += 1
			s[i][j] = 2
			c += 1
			ver[flag].append(i) #d[i][0])
			i = j #d[j][0]
			j = 0

		else:
			j += 1
	i += 1
	j = 0
	
# print(ver)

temp = []
m = len(ver)
y = _j
# print(y)

if (m == 1):
	t_count = 0
	p = y
	while p < len(ver[m-1]):
		temp.append(ver[m-1][p])
		p += 1
		t_count += 1
	if t_count < len(ver[m-1]):
		u = 0
		while (u < y):
			temp.append(ver[m-1][u])
			u += 1
else:
	while y < len(ver[m-1]):
		# print(ver[flag-1][y])
		# print("i", i)

		if ver[m-1][y] == ver[m-1][0]: #d[i][0]:
			t_count = 0
			p = y
			while p < len(ver[m-1]):
				temp.append(ver[m-1][p])
				p += 1
				t_count += 1
			if t_count < len(ver[m-1]):
				u = 0
				while (u < y):
					temp.append(ver[m-1][u])
					u += 1
		y += 1

# print(temp)

ans = v[temp[j]]
for j in range(1,len(temp)):
	ans += v[temp[j]][k-2]
# print(ans)

f = open('output.txt', 'w')
f.write(str(ans))

f.close()