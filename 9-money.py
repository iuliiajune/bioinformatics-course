# 9-money

f = open('input.txt')

M = int(f.readline())
arr = f.readline()

f.close()

t = arr.split(',')
countCoins = len(t)

c = []
for i in range(countCoins):
	c.append(int(t[i]))

bestNumCoins = []
bestNumCoins.append(0)

for m in range(1, M+1):
	bestNumCoins.append(M)

	for i in range(countCoins):
		if m >= c[i]:
			if bestNumCoins[m-c[i]] + 1 < bestNumCoins[m]:
				bestNumCoins[m] = bestNumCoins[m-c[i]] + 1

#print("bestNumCoins", bestNumCoins)
#print(bestNumCoins[M])

# write in file
f = open('output.txt', 'w')
f.write(str(bestNumCoins[M]))

f.close()