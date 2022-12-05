#dec1 1

file1 = open('input.txt', 'r')
lines = file1.readlines()

count = 0
maxNum = 0 
for line in lines:
	thisLine = line.strip()
	if line.strip():
		count += int(thisLine)
	else:
		if count > maxNum:
			maxNum = count
		count = 0

print(maxNum)
