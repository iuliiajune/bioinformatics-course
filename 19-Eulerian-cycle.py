# 19-Eulerian-cycle

# input data
f = open('input.txt')
v = f.readlines()
f.close()

n = len(v)

edge = 0 # count of edges
w = []
d = []
for i in range(n):
	w.append(v[i].split(' -> '))
	d.append([int(w[i][0])])

	w[i][1] = w[i][1].split(',')
	for y in range(len(w[i][1])):
		d[i].append(int(w[i][1][y]))
		edge += 1 

# print(d)
# print(edge)

k = max(n, d[n-1][0] + 1)

matr = [[0 for i in range(k)] for j in range(k)]

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

	while j < k: #n:
		if matr[i][j] == 1:
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
			matr[i][j] = 2
			c += 1
			ver[flag].append(i) #d[i][0])
			i = j #d[j][0]
			j = 0

		else:
			j += 1
	i += 1
	j = 0
# print(ver)

m = len(ver)

ans = ''
i = m-1
start = str(ver[i][0])

for j in range(len(ver[i])):
	ans += str(ver[i][j]) + '->'
start = str(ver[i][0])
ans += start

# print(ans)

f = open('output.txt', 'w')
f.write(str(ans))

f.close()