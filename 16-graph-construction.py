# 16-graph-construction

# input data
f = open('input.txt')

data = f.readlines()

f.close()

n = len(data)

pattern = []
for i in range(n):
    pattern.append(str(data[i]))

k = len(pattern[0]) - 1

s = [[0 for i in range(n)] for j in range(n)]

flag = 0

f = open('output.txt', 'w')
f = open('output.txt', 'a')

t = ''
for i in range(n):
	flag = 0
	t = pattern[i][0:k] + " -> "
	for j in range(n):
		if pattern[i][1:k] == pattern[j][0:k-1]:
			s[i][j] = 1
			
			if (flag == 0):
				t += pattern[j][0:k]
				flag +=1 
			else:
				t += "," + pattern[j][0:k]
	if (flag != 0):
		f.write(t + "\n")
		#print(t)

f.close()