# Think that Genom and Pattern are piece of DNA
# Genom and Pattern are "good" string = consist only "A", "C", "G", "T" letters

# 3-count-pattern
f = open('input.txt')

Genom = f.readline()
Pattern = f.readline()

f.close()

LenGenom = len(Genom)
LenPattern = len(Pattern)

countPattern = 0
positionPattern = ''

for i in range(LenGenom - LenPattern + 1):
  count = i
  j = 0
  flag = 0

  while j < LenPattern:
    if Genom[count] == Pattern[j]:
      j += 1
      count += 1
    else:
      flag = 1
      break

  if flag == 0 and j == LenPattern:
    countPattern += 1
    #positionPattern += str(i + 1) + ' '

f = open('output.txt', 'w')
f.write(str(countPattern))

f.close()