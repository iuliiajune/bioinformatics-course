# 11-longest-common-subsequence-problem

# input data
f = open('input.txt')

v = f.readline()
w = f.readline()

n = len(v) - 1
m = len(w)

s = [[0 for i in range(m+1)] for t in range(n+1)]
#print(s)

b = [[0 for i in range(m+1)] for t in range(n+1)]
#print(b)

for i in range(1,n+1):
	for j in range(1, m+1):
		if v[i-1] == w[j-1]:
			s[i][j] = s[i-1][j-1] + 1
			b[i][j] = 0 # диагональ
		else:
			#s[i][j] = max(s[i-1][j] , s[i][j-1])
			if s[i-1][j] >= s[i][j-1]:
				s[i][j] = s[i-1][j]
				b[i][j] = 1 # up
			else:
				s[i][j] = s[i][j-1]
				b[i][j] = 2 # left
				
		#print(s[i], i)	

#print("\n")		
#for i in range(0, n+1):
#	print(s[i])
	
#print("\n")		
#for i in range(0, n+1):
#	print(b[i])
	
q = s[n][m]
#print(q)

ans = ''
i = n
j = m
while (i != 0) & (j !=0):
	if b[i][j] == 0:
		ans += w[j-1]#v[i-1]
		i -= 1
		j -= 1
		
	else:
		if b[i][j] == 1:
			i -= 1
		else:
			j -= 1

#print(ans)

res = ''
for y in reversed(ans):
	res += y

#print(res)

f = open('output.txt', 'w')
f.write(str(res))

f.close()