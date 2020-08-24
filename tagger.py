#functionality: return a list of tags given a piece of text



import spacy

nlp = spacy.load("en_core_web_sm")

def get_tags(text):
	tags = []
	doc = nlp(text)

	for token in doc:
		
		if token.pos_ == "ADJ" or token.pos_ == "VERB" or token.pos_ == "PROPN" or token.pos_ == "NOUN":
			tags.append(token.lemma_)

	tags = list(set(tags))

	return tags






