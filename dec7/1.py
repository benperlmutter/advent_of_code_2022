#dec1 1

file1 = open('sample_input.txt', 'r')
# file1 = open('input.txt', 'r')
lines = file1.readlines()

def my_function():
	print('this is the function')

def my_recurse(varName):
	if varName == 0:
		return 1
	else:
		return varName * my_recurse(varName-1)

def processLine(el):
	size = len(el)
	if el[0] == "$":
		print(el[0])

for line in lines:
	splLine = line.split(" ")
	# print(splLine)
	processLine(splLine)