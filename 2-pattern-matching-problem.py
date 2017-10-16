# Think that Genom and Pattern are piece of DNA
# Genom and Pattern are "good" string = consist only "A", "C", "G", "T" letters

# input data
Genom = str(input())
Pattern = str(input())

LenGenom = len(Genom)
LenPattern = len(Pattern)

positionPattern = ''

for i in range(LenGenom):
  count = i
  j = 0
  flag = 0
  while j < LenPattern and count < LenGenom:
    if Genom[count] == Pattern[j]:
      j += 1
      count += 1
    else:
      flag = 1
      break
  if flag == 0 and count < LenGenom:
    positionPattern += str(i + 1) + ' '

print(positionPattern)