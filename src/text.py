# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="aditya"
__date__ ="$23 Jan, 2011 4:56:11 PM$"
class ReadText:
    def __init__(self,filename="taggerText"):
        inputFile=open(filename,"r")
        self.readAll=inputFile.read()
        inputFile.close()