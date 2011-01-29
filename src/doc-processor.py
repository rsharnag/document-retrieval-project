# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="aditya"
__date__ ="$27 Jan, 2011 11:09:18 PM$"

#import nltk
import tagger
import generalisation

class DocProcessor:

    def __init__(self):
       self.taggerinst = tagger.Tagger(False)

    def process(self, filename = "taggerText"):
        wordlist = self.taggerinst.classify(filename)
        output = open('output','w')
        output.write(str(wordlist) + '\n')
        i = 0
        generalizedWordList = []
        while i < 3:
            generalizedWordList.extend(generalisation.generalisation(wordlist[i]))
            i = i+1
        #print wordlist
        output.write(str(generalizedWordList))
        output.close()

doc_processor = DocProcessor()
doc_processor.process()
print "Finished"