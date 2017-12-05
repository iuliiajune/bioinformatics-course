# 15-string-reconstruction

# input data
f = open('input.txt')

data = f.readlines()

f.close()

n = len(data)

pattern = []
for i in range(n):
	pattern.append(str(data[i]))

k = len(pattern[0]) - 1

line = pattern[0][0:k]

for i in range(1, n):
	line += pattern[i][k-1]
	
f = open('output.txt', 'w')
f.write(line)

f.close()