import os
import pickle 

def update_wordlist(words):

	currentfile = open("wordlist.txt","rb")
	currentlist = pickle.load(currentfile)
	currentfile.close()

	for word in words:
		if word not in currentlist:
			currentlist.append(word)

	currentfile = open("wordlist.txt","wb")
	pickle.dump(currentlist, currentfile)
	currentfile.close()
	


def update_storage(text, vector):
	textfile = open("text_storage.txt","a")
	textfile.write(text+"\n")
	textfile.close()

	vecfile = open("vec_storage.txt", "rb")
	current_vec_list = pickle.load(vecfile)
	vecfile.close()

	current_vec_list.append(vector)

	vecfile = open("vec_storage.txt", "wb")
	pickle.dump(current_vec_list, vecfile)
	vecfile.close()

