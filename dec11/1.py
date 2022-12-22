#dec11 1

file1 = open('sample_input.txt', 'r')
# file1 = open('input.txt', 'r')
lines = file1.readlines()

monkeyDict = {}
currentMonkey = 0
for line in lines:
	l = line.split()
	# print(l)
	if len(l) > 1:
		if l[0] == "Monkey":
			currentMonkey = int(l[1][0])
			monkeyDict[currentMonkey] = {}
			monkeyDict[currentMonkey]['items'] = []
			# print(monkeyDict)
		if l[0] == "Starting":
			for i in range(len(l)):
				if i > 1:
			# 		tempItems.append(int(l[i].split(",")[0]))
					monkeyDict[currentMonkey]['items'].insert(0, int(l[i].split(",")[0]))

			# l = len(tempItems)
			# for i in range(l):
			# 	monkeyDict[currentMonkey]['items'].append(tempItems.pop())

		if l[0] == "Operation:":
			monkeyDict[currentMonkey]['operation'] = {}
			monkeyDict[currentMonkey]['operation']['operator'] = l[4]
			monkeyDict[currentMonkey]['operation']['value'] = l[5]
			# print(l[5])

		if l[0] == "Test:":
			monkeyDict[currentMonkey]['test'] = l[3]

		if l[1] == "true:":
			monkeyDict[currentMonkey]['true'] = l[5]

		if l[1] == "false:":
			monkeyDict[currentMonkey]['false'] = l[5]



for key in monkeyDict:
	monkey = monkeyDict[key]
	while len(monkey["items"]) > 0:
		print(monkey["items"].pop())


				# print(l[i])
# print(monkeyDict)
# for key in monkeyDict:
# 	l = len(monkeyDict[key]['items'])
# 	for i in range(l):
# 		print(monkeyDict[key]['items'].pop())

