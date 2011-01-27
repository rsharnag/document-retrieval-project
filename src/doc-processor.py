# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="aditya"
__date__ ="$27 Jan, 2011 11:09:18 PM$"

import nltk
import tagger
import generasation

class DocProcessor:

    def __init__(self):
       self.taggerinst = tagger.Tagger(false)

    def process(self, filename = "taggerText"):
        self.taggerinst.classify(filename)

doc_processor = DocProcessor()
doc_processor.process()
