#dec1 1

# file1 = open('sample_input.txt', 'r')
file1 = open('input.txt', 'r')
lines = file1.readlines()

lineCounter = 1

counter = ""
stackLines = []
moveLines = []
realStack = []
for line in lines:
	splitLine = line.split(" ")
	if counter == "":
		stackLines.append(splitLine)
		if splitLine[0] == '\n':
			counter = " "
	elif counter == " ":
		moveLines.append(splitLine)

for i in range(int(stackLines[-2][-2])):
	realStack.append([])

# for i in stackLines:
# 	print(i)

for row in stackLines[::-1]:
	lineCounter += 1
	# print(row)
	counter = 0
	spaceCounter = 0
	for i in row:
		print("counter {} & spaceCounter {} & i {}".format(counter, spaceCounter, str(i)))
		if len(i) > 1:
			realStack[counter].append(i[1])
			print(realStack[counter])
			counter += 1
		elif i == "" or i == '\n':
			if spaceCounter == 3:
				counter += 1
				spaceCounter = 0
			spaceCounter += 1

# print(realStack[0].pop())

# print(realStack)
i = 1
for x in realStack:
	print("{} {}".format(i,x))
	i+=1

count = 1

for line in moveLines:
	lineCounter += 1
	# print(int(lines[1]))
	# print(line)
	numMoves = int(line[1])
	start = int(line[3])
	end = line[5]
	splitEnd = end.split('\n')
	end = int(splitEnd[0])
	# print("move {} from {} to {}".format(numMoves, start, end))
	# print("{} {} {}".format(numMoves, start, end))
	# print(lineCounter)
	# i = 1
	# for x in realStack:
	# 	print("{} {}".format(i,x))
	# 	i+=1
	for move in range(numMoves):
		# if realStack[start-1]:
		realStack[end-1].append(realStack[start-1].pop())
		# if count > 30 and count <= 37:
		# 	print("in while")
		# 	print("{} {} {}".format(numMoves, start, end))
		# 	print(lineCounter)
		# 	i = 1
		# 	for x in realStack:
		# 		print("{} {}".format(i,x))
		# 		i += 1
	count += 1
		# print("move")

print("end")
# print(realStack)
i = 1
string = ""
for x in realStack:
	print("{} {}".format(i,x))
	string += x[-1]
	i+=1

print(string)

# for stack in realStack:
	# print(stack.pop())
# print(moveLines[-2])
	# n = 3
	# if counter == 1:
	# 	for i in range (0, len(line), n):
	# 		print(line[i:i+n])
	# 		counter +=1
	# if counter == 1:
	# 	for char in line:
	# 		if mod % 2 != 0:

	# 		if char == '\n':
	# 			print('newline')
	# 		elif char == ' ':
	# 			print('space')
	# 		else:
	# 			print(char)
	# 	counter +=1