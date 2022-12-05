#dec1 1

file1 = open('input.txt', 'r')
lines = file1.readlines()


solutionDict = {
	"A": {
	"X":1+3,
	"Y":2+6,
	"Z":3+0
	},
	"B": {
	"Y":2+3,
	"Z":3+6,
	"X":1+0
	},
	"C": {
	"Z":3+3,
	"X":1+6,
	"Y":2+0
	}
}

score = 0
for line in lines:
	thisLine = line.strip()
	splitLine = thisLine.split()
	print(thisLine)
	them = splitLine[0]
	me = splitLine[1]
	score += solutionDict[them][me]
	# print("{} vs {}".format(them, me))
	# print("{} and {}".format(solutionDict[them][me], score))
	# print("Line {}: {}".format(count, line.strip()))

print(score)