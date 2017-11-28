# 10-manhattan-tourist-problem

# input data
f = open('input.txt')

line = f.readline()

t = line.split(' ')
n = int(t[0])
m = int(t[1])

# south value
south = []
for i in range(n):
	south.append(f.readline())
	south[i] = south[i].split(' ')
#print(south)
# "-"	
t = f.readline()

# east value
east = []
for i in range(n+1):
	east.append(f.readline())
	east[i] = east[i].split(' ')
#print(east)
f.close()

for i in range(n):
	for j in range(m+1):
		south[i][j] = int(south[i][j])

for i in range(n+1):
	for j in range(m):
		east[i][j] = int(east[i][j])
	
#print("south", south)
#print("east", east)

s = [[0 for q in range(m+1)] for t in range(n+1)]
#print(s)

for i in range(1, m+1):
	s[0][i] = s[0][i-1] + east[0][i-1]

for i in range(1, n):
	s[i][0] = s[i-1][0] + south[i-1][0]

#print(s)

for i in range(1, n+1):
	for j in range(1, m+1):
		s[i][j] = max(s[i-1][j] +  south[i-1][j], s[i][j-1] + east[i][j-1])

#print(s)
#print(s[n][m])

# write in file
f = open('output.txt', 'w')
f.write(str(s[n][m]))

f.close()