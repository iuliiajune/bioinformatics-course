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

# input data
Text = str(input())
k = int(input())

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

#print(Patterns)
#print(Counts)

# select patterns with max count
for i in range(len(Counts)):
  if Counts[i] == maxCount:
    FreqPattern.append(Patterns[i])

#print(FreqPattern)

# remote duplicates
FinFreqPattern = []
#FinFreqPattern.append(FreqPattern[0])
f = 0
Final = FreqPattern[0] + ' '

for i in range(1, len(FreqPattern)):
  for j in range(i):
    if FreqPattern[j] == FreqPattern[i]:
      f += 1;

  if f == 0:
    #FinFreqPattern.append(FreqPattern[i])
    Final += FreqPattern[i] + ' '

#print(FinFreqPattern)
print(Final)