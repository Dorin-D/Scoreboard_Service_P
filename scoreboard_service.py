def read_scores(file_name):
	file = open(file_name, 'r')
	scores = file.readlines()
	scoreboard = []
	for row in scores:
		entry = row.split()
		#convert score to int to allow sorting
		entry[1] = int(entry[1])
		scoreboard.append(entry)
	file.close()
	return scoreboard
	
def add_score(user, score, file_name):
	file = open(file_name, 'a+')
	file.write(user + " " + str(score))
	file.close()

def partition(list, start, end):
	pivot = list[start][1]
	low = start + 1
	high = end
	
	while True:
		while low <= high and list[high][1] >= pivot:
			high = high - 1
		
		while low <= high and list[low][1] <= pivot:
			low = low + 1

		if low <= high:
			list[low][1], list[high][1] = list[high][1], list[low][1]
		else:
			break
			
	list[start][1], list[high][1] = list[high][1], list[start][1]
	return high
	
def quick_sort(list, start, end):
	if start >= end:
		return
	
	p = partition(list, start, end)
	quick_sort(list, start, p-1)
	quick_sort(list, p+1, end)

#accessing the stored scoreboard
#print(read_scores("scores"))

#adding a new entry
#add_score("Otter_Possum", "13", "scores")

#sorting current scores
#scoreboard = read_scores("scores")
#quick_sort(scoreboard, 0, len(scoreboard)-1)
#print(scoreboard)
