#dec2 2

file1 = open('input.txt', 'r')
lines = file1.readlines()


solutionDict = {
	"X": {
	"A":3+0,
	"B":1+0,
	"C":2+0
	},
	"Y": {
	"A":1+3,
	"B":2+3,
	"C":3+3
	},
	"Z": {
	"A":2+6,
	"B":3+6,
	"C":1+6
	}
}

score = 0
for line in lines:
	thisLine = line.strip()
	splitLine = thisLine.split()
	print(thisLine)
	them = splitLine[0]
	me = splitLine[1]
	score += solutionDict[me][them]
	# print("{} vs {}".format(them, me))
	# print("{} and {}".format(solutionDict[them][me], score))
	# print("Line {}: {}".format(count, line.strip()))

print(score)