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

#print(read_scores("scores"))
add_score("Otter_Possum", "13", "scores")

