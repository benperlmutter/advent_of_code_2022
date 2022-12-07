file1 = open('output.txt', 'r')
lines1 = file1.readlines()

file2 = open('output2.txt', 'r')
lines2 = file2.readlines()

dict1 = {}
for line in lines1:
	dict1[line] = True

rowCount = 1
for line in lines2:
	if dict1.get(line):
		print(rowCount)
		rowCount += 1
	else:
		print(rowCount)
		print(line)
		rowCount += 1