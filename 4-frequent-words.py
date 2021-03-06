# Think that Genom and Pattern are piece of DNA
# Genom and Pattern are "good" string = consist only "A", "C", "G", "T" letters

# functions
def PatternCount(Genom, Pattern):
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

  return countPattern

# 4-frequent-words
f = open('input.txt')

Text = str(f.readline())
k = int(f.readline())
f.close()

LenText = len(Text)

Genom = Text
Patterns = []
Counts = []
FreqPattern = []
maxCount = 0

# compute patterns and its count
for i in range(LenText - k + 1):
  Pattern = Genom[i:i+k]
  #print(Pattern)
  Patterns.append(Pattern)

  y = PatternCount(Text, Pattern)
  Counts.append(y)
  if y > maxCount:
    maxCount = y

# select patterns with max count
for i in range(len(Counts)):
  if Counts[i] == maxCount:
    FreqPattern.append(Patterns[i])

# remote duplicates
FinFreqPattern = []
#FinFreqPattern.append(FreqPattern[0])

Final = ''

for i in range(len(FreqPattern)):
  f = 0
  for j in range(i):
    if FreqPattern[i] == FreqPattern[j]:
      f += 1;

  if f == 0:
    #FinFreqPattern.append(FreqPattern[i])
    Final += FreqPattern[i] + ' '

#print(FinFreqPattern)
#print(Final)
f = open('output.txt', 'w')
f.write(str(Final))

f.close()