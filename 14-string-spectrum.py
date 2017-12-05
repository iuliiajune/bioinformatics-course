# 14-string-spectrum

# input data
f = open('input.txt')

k = int(f.readline())
v = str(f.readline())

f.close()

n = len(v)

f = open('output.txt', 'w')
f = open('output.txt', 'a')

for i in range(n-k+1):
	t = v[i:i+k]
	f.write(t + '\n')

f.close()