#dec9 2
from collections import defaultdict

def moveRope(coord, direction, knot, gridCurrent, gridPath):
	h = gridCurrent[knot]
	t = gridCurrent[knot+1]
	if coord == "x":
		if h['y'] - t['y'] > 1:
			t['y'] = h['y']-1
		elif t['y'] - h['y'] > 1:
			t['y'] = h['y']+1
		if direction == "add":
			if knot == 0:
				h['x'] += 1
			if abs(h['x'] - t['x']) > 1:
				if abs(h['y'] - t['y']) >= 1:
					t['y'] = h['y']
				t['x'] += 1
				gridCurrent[knot+1] = t
				gridCurrent[knot] = h
				gridPath[knot+1].setdefault(""+str(t['x'])+","+str(t['y']), 0)
				gridPath[knot+1][""+str(t['x'])+","+str(t['y'])] += 1
		else:
			if knot == 0:
				h['x'] -= 1
			if abs(h['x'] - t['x']) > 1:
				if abs(h['y'] - t['y']) >= 1:
					t['y'] = h['y']
				t['x'] -= 1
				gridCurrent[knot+1] = t
				gridCurrent[knot] = h
				gridPath[knot+1].setdefault(""+str(t['x'])+","+str(t['y']), 0)
				gridPath[knot+1][""+str(t['x'])+","+str(t['y'])] += 1

	else:
		if h['x'] - t['x'] > 1:
			t['x'] = h['x']-1
		elif t['x'] - h['x'] > 1:
			t['x'] = h['x']+1
		if direction == "add":
			if knot == 0:
				h['y'] += 1
			if abs(h['y'] - t['y']) > 1:
				if abs(h['x'] - t['x']) >= 1:
					t['x'] = h['x']
				t['y'] += 1
				gridCurrent[knot+1] = t
				gridCurrent[knot] = h
				gridPath[knot+1].setdefault(""+str(t['x'])+","+str(t['y']), 0)
				gridPath[knot+1][""+str(t['x'])+","+str(t['y'])] += 1
			
		else:
			if knot == 0:
				h['y'] -= 1
			if abs(h['y'] - t['y']) > 1:
				if abs(h['x'] - t['x']) >= 1:
					t['x'] = h['x']
				t['y'] -= 1
				gridCurrent[knot+1] = t
				gridCurrent[knot] = h
				gridPath[knot+1].setdefault(""+str(t['x'])+","+str(t['y']), 0)
				gridPath[knot+1][""+str(t['x'])+","+str(t['y'])] += 1


def printGrid(sizeY, sizeX, startY, startX, currentGrid):
	for y in range(sizeY+1):
		# print('this is y {}'.format(y))
		line = ""
		for x in range(sizeX):
			line += "."
			for key in currentGrid:
				if (currentGrid[key]['y']+startY == (sizeY-y)) and (currentGrid[key]['x']+startX == x):
					line = line[:(len(line)-1)]
					line += str(key)
					# line = line[:(len(line)-1)]
					# if line[-1:] == ".":
						# line += str(key)
						
				# else:
				# 	line += "."
						
		print(line)






numKnots = 9

gridPath = defaultdict(dict)
gridCurrent = defaultdict(dict)

file1 = open('sample_input2.txt', 'r')
# file1 = open('input.txt', 'r')
lines = file1.readlines()

moveList = []

for line in lines:
	l = line.split(" ")
	d = l[0]
	n = l[1].split("\n")[0]
	moveList.append((d,n))

# for i in moveList:
# 	print(moveList[:1])
# 	moveList = moveList[1:]

for i in range(numKnots+1):
	gridPath[i] = {}
	gridPath[i]['0,0'] = 1
	gridCurrent[i] = {}
	gridCurrent[i]['x'] = 0
	gridCurrent[i]['y'] = 0

for i in moveList:
	thisMove = moveList[:1]
	# print(thisMove[0][0])
	d = thisMove[0][0]
	n = int(thisMove[0][1])
	# print(d)
	# print(n)
	for numMoves in range(n):
		for knot in range(numKnots):
			printGrid(26, 21, 5, 12, gridCurrent)
			# print(knot)
			h = gridCurrent[knot]
			# print(h)
			t = gridCurrent[knot+1]
			# print(t)
			if d == "R":
				print('move right')
				moveRope("x", "add", knot, gridCurrent, gridPath)
			elif d =="U":	
				print('move up')
				moveRope("y", "add", knot, gridCurrent, gridPath)
			elif d =="L":
				print('move left')
				moveRope("x", "subtract", knot, gridCurrent, gridPath)
			else:
				print('move down')
				moveRope("y", "subtract", knot, gridCurrent, gridPath)

			# print(gridCurrent[knot])
			# print(gridCurrent[knot+1])
			# print('\n')

	moveList = moveList[1:]

print(gridPath)
print(numKnots)
print(len(gridPath[numKnots]))