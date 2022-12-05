#dec1 1

# file1 = open('sample_input.txt', 'r')
file1 = open('input.txt', 'r')
lines = file1.readlines()
count = 0
newCount = 0
lineNum = 0
oldStr = ""
newStr = ""
newerCount = 0
for line in lines:
	lineNum +=1
	thisLine = line.strip()
	elves = thisLine.split(',')
	elf1 = elves[0].split('-')
	elf2 = elves[1].split('-')
	elf11 = int(elf1[0])
	elf12 = int(elf1[1])
	elf21 = int(elf2[0])
	elf22 = int(elf2[1])
	elf1Str = ","
	elf2Str = ","
	for i in range(elf11, elf12+1):
		elf1Str += str(i)+","
	for g in range(elf21, elf22+1):
		elf2Str += str(g)+","

	# print("elf1 {}".format(elf1Str))
	# print("elf2 {}".format(elf2Str))

	if elf1Str in elf2Str:
		oldStr += "elf1 in elf2 {} {}".format(elf1Str, elf2Str)+'\n'
		if lineNum == 991:
			print("elf1 in elf2 {} {}".format(elf1Str, elf2Str))
		# print("elf1 in elf2 {} {}".format(elf1Str, elf2Str))
		count +=1
		print(lineNum)
	elif elf2Str in elf1Str:
		oldStr += "elf2 in elf1 {} {}".format(elf2Str, elf1Str)+'\n'
		if lineNum == 991:
			print("elf1 in elf2 {} {}".format(elf1Str, elf2Str))
		# print("elf2 in elf1 {} {}".format(elf2Str, elf1Str))
		count +=1
		print(lineNum)

	if elf1Str.find(elf2Str) > -1:
		newStr += "elf2 in elf1 {} {}".format(elf2Str, elf1Str)+'\n'
		newCount += 1
		# print(lineNum)
	elif elf2Str.find(elf1Str) > -1:
		newStr += "elf1 in elf2 {} {}".format(elf1Str, elf2Str)+'\n'
		newCount += 1
		# print(lineNum)

	if ((elf11 <= elf21) and (elf12 >= elf21)) or ((elf11 <= elf22) and (elf12 >= elf22)) or ((elf21 <= elf11) and (elf22 >= elf11)) or ((elf21 <= elf12) and (elf22 >= elf12)):
		newerCount += 1
		# print(lineNum)


# print(newStr)
# print("final count is {}".format(newCount))

test1 = "4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,"
test2 = "4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,"

# print(test1.find(test2))
print(count)
print(newCount)
print(newerCount)


