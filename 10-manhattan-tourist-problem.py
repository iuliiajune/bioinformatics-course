# 10-manhattan-tourist-problem

# input data
f = open('input.txt')

line = f.readline()

t = line.split(' ')
n = int(t[0])
m = int(t[1])

#south value
south = []
for i in range(n):
	south.append(f.readline())
	south[i] = south[i].split(' ')

# "-"	
t = f.readline()

#east value
east = []
for i in range(n + 1):
	east.append(f.readline())
	east[i] = east[i].split(' ')
		
f.close()

for i in range(n):
	for j in range(m+1):
		south[i][j] = int(south[i][j])
		east[j][i] = int(east[j][i])
	
print(south)
print(east)