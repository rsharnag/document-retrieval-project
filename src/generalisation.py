# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="aditya & rahul"
__date__ ="$26 Jan, 2011 4:13:20 PM$"

from nltk.corpus import wordnet as wn
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
    while(len(currentWordList)>2):
        generalizedWords = []
        currShortest_Dist = 2
        currentWord = currentWordList.pop()
        for otherWord in currentWordList:
            for currentWordSyn in synWords[currentWord]:
                for ithWordSyn in synWords[otherWord]:
                    short_dist = ithWordSyn.shortest_path_distance(currentWordSyn)
                    if (short_dist != None and short_dist < currShortest_Dist):
                        currShortest_Dist = short_dist
                        generalizedWords = []
                        generalizedWords.extend(ithWordSyn.common_hypernyms(currentWordSyn))
                    if (short_dist != None and short_dist == currShortest_Dist):
                        generalizedWords.extend(ithWordSyn.common_hypernyms(currentWordSyn))

            generalisedWordList.extend([currentWord,otherWord])
            if(len(generalizedWords)!=0):
                currentWordList.remove(otherWord)
                l=[]
                for syns in generalizedWords:
                    l.extend(syns.lemma_names)
                generalisedWordList.extend(l)
    generalisedWordList=list(set(generalisedWordList))
    return generalisedWordList