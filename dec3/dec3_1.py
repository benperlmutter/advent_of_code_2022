#dec1 1

file1 = open('input.txt', 'r')
lines = file1.readlines()

abc_s = "abcdefghijklmnopqrstuvwxyz"

scoreDict = {}

for char in range(len(abc_s)):
	scoreDict[abc_s[char]] = char+1
	# print(scoreDict)

count = 0
for line in lines:
	dict1 = {}
	thisLine = line.strip()
	halfLength = int(len(thisLine))/2
	for char in thisLine[0:int(halfLength)]:
		dict1[char] = True

	shared = ""

	for char in thisLine[int(halfLength):len(thisLine)]:
		if dict1.get(char) == True:
			dict1[char] = False
			shared = char
			count += scoreDict[shared.lower()]
			thisScore = scoreDict[shared.lower()]
			if shared == shared.upper():
				count += 26 
				thisScore += 26
			print("the letter is {} and the score is {}".format(shared,thisScore))

print(count)


# solutionDict = {
# 	"A": {
# 	"X":3,
# 	"Y":6,
# 	"Z":0
# 	},
# 	"B": {
# 	"Y":3,
# 	"Z":6,
# 	"X":0
# 	},
# 	"C": {
# 	"Z":3,
# 	"X":6,
# 	"Y":0
# 	}
# }

# score = 0
# for line in lines:
# 	thisLine = line.strip()
# 	splitLine = thisLine.split()
# 	them = splitLine[0]
# 	me = splitLine[1]
# 	if me == "X":
# 		score += 1
# 	elif me == "Y":
# 		score += 2
# 	elif me == "Z":
# 		score += 3

# 	score += solutionDict[them][me]
# 	# print("{} vs {}".format(them, me))
# 	print("{} and {}".format(solutionDict[them][me], score))
# 	# print("Line {}: {}".format(count, line.strip()))

# print(score)