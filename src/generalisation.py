# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="aditya"
__date__ ="$26 Jan, 2011 4:13:20 PM$"

from nltk.corpus import wordent as wn
def createSynsetDict(wordList):
    """Creates a dictionary of synonyms of given wordlist"""
    synWords={}
    for word in wordList:
        synWords[word] = wn.synsets(word)
    return synWords

def generalisation(originalWordList):
    generalisedWordList=[]
    currentWordList = originalWordList
    synWords = createSynsetDict(originalWordList)
    while(currentWordList.size()>2):
        generalizedWords = []
        currentWord = currentWordList.pop()
        for otherWord in currentWordList:
            for currentWordSyn in synWords[currentWord]:
                for ithWordSyn in synWords[otherWord]:
                    short_dist = ithWordSyn.shortest_path_distance(currentWordSyn)
                    if (short_dist != None and short_dist <= 2):
                        generalizedWords.append(ithWordSyn.common_hypernyms(currentWordSyn))
           
            generalisedWordList.extend([currentWord,otherWord])
            if(len(generalizedWords)!=0):
                currentWordList.remove(otherWord)
                l=[]
                for syns in generalisedWords:
                    l.append(syns.lemma_names)
                generalisedWordList.append(l)
    generalisedWordList=list(set(generalisedWordList))
    return generalisedWordList