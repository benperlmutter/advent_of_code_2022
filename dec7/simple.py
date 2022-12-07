file1 = open('simple_input.txt', 'r')

lines = file1.readlines()

def sumDir(a):
	if a[0] == []:
		collector = 0
		for num in a[1]:
			collector += num
		return collector
	else:
		acc = 0
		recursiveNum = 0
		for num in a[1]:
			acc += num
			print(acc)
		for d in a[0]:
			recursiveNum += sumDir(d)
			print(recursiveNum)

		return acc + recursiveNum

b = [[],[3]]
d = [[],[6,4]]
dirList = [[b,d],[1,2,4]]

print(sumDir(dirList))
