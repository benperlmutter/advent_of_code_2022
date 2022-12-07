#dec1 1

def sumDir(dirDict,key):
	a = dirDict[key]
	acc = 0
	if a[0] == []:
		collector = 0
		for num in a[1]:
			collector += num
		return collector
	else:
		for d in a[0]:
			acc += sumDir(dirDict,d)
	for n in a[1]:
		acc += n

	return acc


# file1 = open('simple_input.txt', 'r')
# file1 = open('sample_input.txt', 'r')
file1 = open('input.txt', 'r')
lines = file1.readlines()

dirDict = {"/":[[],[]]}

currDir = []
acc = 0
for line in lines:
	el = line.split(" ")
	if el[0] == "$":
		acc = 0
		if el[1] == "cd":
			if el[2] == "..\n":
				currDir.pop()
			else:
				currDir.append(el[2].split("\n")[0])
				strDir = "#".join(currDir)
				# print(strDir)
				if dirDict.get(strDir) == None:
					# print('here')
					dirDict[strDir] = [[],[]]
	elif el[0] == "dir":
		stringCurrDir = "#".join(currDir)
		newDir = currDir.copy()
		newDir.append(el[1].split("\n")[0])
		strDir = "#".join(newDir)
		dirDict[stringCurrDir][0].append(strDir)
		# print(strDir)
	else:
		# print(currDir)
		strDir = "#".join(currDir)
		dirDict[strDir][1].append(int(el[0]))

	# print(splLine)
# print(dirDict)

sumTotal = 0

for key in dirDict:
	# print("{} dir has {} bytes".format(key, sumDir(dirDict,key)))
	tot = sumDir(dirDict,key)
	if tot <= 100000:
		sumTotal += tot

print(sumTotal)