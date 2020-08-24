import os
import pickle

def cosine(v1, v2):

	if len(v1) >= len(v2):
		big = v1
		smol = v2
	else:
		big = v2
		smol = v1

	diff = len(big) - len(smol)


	for i in range(diff):
		smol.append(0)



	cos = 0
	for i in range(len(v1)):
		cos = cos + v1[i]*v2[i]

	return cos

def create_vector(tags):
	vector = []
	currentfile = open("wordlist.txt","rb")
	currentwords = pickle.load(currentfile)
	currentfile.close()

	for word in currentwords:
		if word in tags:
			vector.append(1)
		else:
			vector.append(0)

	return vector	



def reset():
		textfile = open("text_storage.txt","w")
		vecfile = open("vec_storage.txt","wb")
		textfile.write("")#empty storage file
		pickle.dump([], vecfile)#empty vectors list
		textfile.close()
		vecfile.close()

		wordfile = open("wordlist.txt","wb")#empty the wordlist
		pickle.dump([], wordfile)
		wordfile.close()