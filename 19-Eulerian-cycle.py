# 19-Eulerian-cycle

# input data
f = open('input12.txt')
v = f.readlines()
f.close()

# print(v)
n = len(v)

edge = 0 # count of edges
w = []
d = []
for i in range(n):
	w.append(v[i].split(' -> '))
	d.append([int(w[i][0])])
	# print(w)
	w[i][1] = w[i][1].split(',')
	for y in range(len(w[i][1])):
		d[i].append(int(w[i][1][y]))
		edge += 1 

# print(d)
print(edge)

matr = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
	for j in range(1,len(d[i])):
		matr[d[i][0]][d[i][j]] = 1

# print("\n")		
# for i in range(n):
# 	print(matr[i])

i = 0
j = 0
c = 0
ver = []
flag = -1
matr_flag = -1
while c < edge:
	matr_flag = -1
	# flag += 1
	# ver.append([])
	# c = 0
	# while i < n:
	while j < n:
		if matr[i][j] == 1:
			matr_flag += 1
			if matr_flag == 0:
				flag += 1
				ver.append([])
			matr[i][j] = 2
			c += 1
			ver[flag].append(d[i][0])
			i = d[j][0]
			j = 0
		# elif matr[i][j] == 2:
		# 	matr[i][j] = -1
		# 	c += 1
		# 	ver.append(d[i][0])
		# 	i = d[j][0]
		# 	j = 0
		# elif matr[i][j] == 0:
		# 	j += 1
		else:
			j += 1
	i += 1
	j = 0
print(ver)
print(c)

m = len(ver)

ans = ''
i = m-1
start = str(ver[i][0])
while i > -1:
	# for j in range(len(ver[i])):
	while ver[i][j] != start:
		j += 1
	ans += str(ver[i][j]) + '->'
	start = str(ver[i][0])
	ans += start
	i -= 1 

print(ans)

# f = open('output.txt', 'w')
# f.write(str(s_max) + "\n")
# f.write(str(res2)+ "\n")
# f.write(str(res1))

# f.close()