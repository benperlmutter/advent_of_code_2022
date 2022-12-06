#dec1 1

# file1 = open('sample_input.txt', 'r')
file1 = open('input.txt', 'r')
lines = file1.readlines()

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

for row in stackLines[::-1]:
	# print(row)
	counter = 0
	spaceCounter = 0
	for i in row:
		if len(i) > 1:
			realStack[counter].append(i[1])
			counter += 1
		elif i == "" or i == '\n':
			spaceCounter += 1
			if spaceCounter == 3:
				counter += 1
				spaceCounter = 0

print(realStack)



# print(stackLines)
# print(moveLines)
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