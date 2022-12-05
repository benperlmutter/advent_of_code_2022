#dec1 2

file1 = open('input.txt', 'r')
lines = file1.readlines()

count = 0
maxNum = 0
secondNum = 0
thirdNum = 0 
for line in lines:
	thisLine = line.strip()
	if line.strip():
		count += int(thisLine)
	else:
		if count > maxNum:
			thirdNum = secondNum
			secondNum = maxNum
			maxNum = count
		elif count > secondNum:
			thirdNum = secondNum
			secondNum = count
		elif count > thirdNum:
			thirdNum = count
		count = 0

print(maxNum+secondNum+thirdNum)