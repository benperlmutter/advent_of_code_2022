#dec9 2
from collections import defaultdict

def moveRope(coord, direction, knot, gridCurrent, gridPath):
	h = gridCurrent[knot]
	t = gridCurrent[knot+1]
	if coord == "x":
		if direction == "add":
			if knot == 0:
				h['x'] += 1
			if abs(h['x'] - t['x']) > 1:
				print('here')
				if abs(h['y'] - t['y']) >= 1:
					t['y'] = h['y']
				t['x'] += 1
				gridCurrent[knot+1] = t
				gridCurrent[knot] = h
				gridPath.setdefault(""+str(t['x'])+","+str(t['y']), 0)
				gridPath[""+str(t['x'])+","+str(t['y'])] += 1
		else:
			if knot == 0:
				h['y'] -= 1
			if abs(h['x'] - t['x']) > 1:
				if abs(h['y'] - t['y']) >= 1:
					t['y'] = h['y']
				t['x'] -= 1
				gridCurrent[knot+1] = t
				gridCurrent[knot] = h
				gridPath.setdefault(""+str(t['x'])+","+str(t['y']), 0)
				gridPath[""+str(t['x'])+","+str(t['y'])] += 1

	else:
		if direction == "add":
			if knot == 0:
				h['y'] += 1
			if abs(h['y'] - t['y']) > 1:
				if abs(h['x'] - t['x']) >= 1:
					t['x'] = h['x']
				t['y'] += 1
				gridCurrent[knot+1] = t
				gridCurrent[knot] = h
				gridPath.setdefault(""+str(t['x'])+","+str(t['y']), 0)
				gridPath[""+str(t['x'])+","+str(t['y'])] += 1
			
		else:
			if knot == 0:
				h['y'] -= 1
			if abs(h['y'] - t['y']) > 1:
				if abs(h['x'] - t['x']) >= 1:
					t['x'] = h['x']
				t['y'] -= 1
				gridCurrent[knot+1] = t
				gridCurrent[knot] = h
				gridPath.setdefault(""+str(t['x'])+","+str(t['y']), 0)
				gridPath[""+str(t['x'])+","+str(t['y'])] += 1

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
			print(knot)
			h = gridCurrent[knot]
			print(h)
			t = gridCurrent[knot+1]
			print(t)
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

			print(gridCurrent[knot])
			print(gridCurrent[knot+1])
			print('\n')

	moveList = moveList[1:]

print(gridPath)