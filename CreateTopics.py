import lda
import numpy as np
from Parser2 import parser
from index import *
from counter import countDocs

parser(encode="cp1252")
decoding, code = createIndexMap(encode="cp1252")
createIndexFiles(encode="cp1252", coding=code)
del code #Borramos code para liberar memoria
vocabs = np.array(list(decoding.keys()))
numWords, numDocs = countDocs(encode="cp1252")
X = np.ndarray((1000, len(decoding)), int)

with open("raw.es\\Indexados\\spanishText_480000_485000_PARSED_INDEXED", encoding="cp1252") as arch:
	for num, line in enumerate(arch):
		if num == 1000:
			break
		for word in line.split():
			X[num][int(word)] += 1
model = lda.LDA(n_topics=20, n_iter=500, random_state=1)
model.fit(X)
topic_word = model.topic_word_
for i, topic_dist in enumerate(topic_word):
    topic_words = np.array(tuple(str(n) for n in range(len(decoding))))[np.argsort(topic_dist)][:-30:-1]
    print('Topic {}: {}'.format(i, ' '.join([decoding[int(n)] + "," for n in topic_words])))

   