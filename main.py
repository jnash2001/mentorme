from update import update_wordlist, update_storage

from tagger import get_tags

from operations import create_vector, reset, cosine

import os

import pickle

from linecache import getline

def entry_taker():
	text = input("enter journal entry: ")
	tags = get_tags(text)
	update_wordlist(tags)
	vector = create_vector(tags)

	update_storage(text, vector)
	
	print("your entry has been stored")

	return vector


def reccomender(vector):
	#initialise tupe : (score, id)

	geiger = [0, 0]

	#load the stored vectors as a list
	stored_vecs = open("vec_storage.txt", "rb")
	veclist = pickle.load(stored_vecs)

	#for all vectors, take cosine, keep position of highest one till calulated noted
	for i in range(len(veclist)-1):
		cos = cosine(vector, veclist[i])
		

		if cos >= geiger[0]:
			geiger[0] = cos
			geiger[1] = i
	
	#return the message with the highest cosine

	line = getline("text_storage.txt", geiger[1]+1)

	outmessage = "You had a similar journal entry in \n {}".format(line)

	return outmessage

reset()
#vector = entry_taker()
#print(reccomender(vector))





