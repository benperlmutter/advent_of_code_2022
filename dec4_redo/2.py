#dec1 1

# file1 = open('sample_input.txt', 'r')
file1 = open('input.txt', 'r')
lines = file1.readlines()

counter = 0

for line in lines:
	line = line.split("\n")[0]
	elfLine = line.split(",")
	# print(elfLine)
	elf1 = elfLine[0].split("-")
	elf2 = elfLine[1].split("-")
	# print(elf1)
	# print(elf2)
	elf1List = []
	elf1List.extend(range(int(elf1[0]), int(elf1[1])+1))
	elf1Set = set(elf1List)
	elf2List = []
	elf2List.extend(range(int(elf2[0]), int(elf2[1])+1))
	elf2Set = set(elf2List)
	if elf1Set.intersection(elf2Set) or elf2Set.intersection(elf1Set):
		counter += 1

print(counter)