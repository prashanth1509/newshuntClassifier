import os, fnmatch
import nltk
from textblob.classifiers import NaiveBayesClassifier
from nltk.corpus import stopwords
import pprint
import json
import urllib

stop = stopwords.words('english')

class Classifyar:
    contents = ""

    def __init__(self, learning_link):
        #learning_link = "https://api.myjson.com/bins/1s1xp"
        f = urllib.urlopen(learning_link)
        self.contents = f.read()

    def removeStops(src):
    	filtered_words = [w for w in src.split() if not w in stopwords.words('english')]
    	return ' '.join(filtered_words)

    def clean(src):
    	return ''.join([i if ord(i) < 128 else ' ' for i in src])

    def getClassifier(self):
        trainer = []
        data = json.loads(self.contents)

        for topic in data:
            for line in data[topic]:
                trainer.append((line, topic))

        cl = NaiveBayesClassifier(trainer)
        return cl

