#dec9 2

# file1 = open('sample_input.txt', 'r')
file1 = open('input.txt', 'r')
lines = file1.readlines()

rows = []
columns = {}
visibleTrees = []

row1 = 0

for line in lines:
	# print(line)
	columnIter = 0
	rows.append(line.split('\n')[0])
	if row1 == 0:
		for char in line:
			if char != '\n':
				columns[columnIter] = char
				columnIter += 1
		row1 += 1
	else:
		for char in line:
			if char != '\n':
				columns[columnIter] += char
				columnIter += 1

# print(rows)
rowIter = 0
rowSize = len(rows)
maxScore = 0
for r in rows: 
	for columnIter in columns:
		c = columns[columnIter]
		print("r is {}".format(r))
		t1 = vTree(r[columnIter],c[::-1][len(c)-rowIter:])
		print("# is {} and string is {} and score is {}".format(r[columnIter],c[::-1][len(c)-rowIter:], t1))
		t2 = vTree(r[columnIter],columns[columnIter][rowIter+1:])
		print("# is {} and string is {} and score is {}".format(r[columnIter],columns[columnIter][rowIter+1:], t2))
		t3 = vTree(r[columnIter],r[::-1][len(r)-columnIter:])
		print("# is {} and string is {} and score is {}".format(r[columnIter],r[::-1][len(r)-columnIter:], t3))
		t4 = vTree(r[columnIter],r[columnIter+1:])
		print("# is {} and string is {} and score is {}".format(r[columnIter],r[columnIter+1:], t4))
		score = t1 * t2 * t3 * t4
		print("scores are {}{}{}{}".format(t1,t2,t3,t4))
		if score > maxScore:
			maxScore = score
			# print(r[columnIter])
			# print("the 4 pieces are \n{}\n{}\n{}\n{}\n".format(columns[columnIter][:rowIter], columns[columnIter][rowIter+1:], r[:len(r)-columnIter:-1], r[columnIter+1:]))

	rowIter += 1
	
print(maxScore)	

print(columns)

