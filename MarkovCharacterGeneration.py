# Code to generate characters based on input sentence. All case will be converted to lowercase, and output will be a list of characters

import pandas as pd
import numpy as np

class markovChar:
    def __init__(self,text):
        self.allowedChars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','o','n','p','q','r','s','t','u','v','w','x','y','z']
        self.text = text
        self.textCharList = []
        self.predicted = []

    # Convert the input text into plain list of alphabets
    def charList(self):
        text = self.text
        list = []
        for i in text:
            if (i in self.allowedChars):
                list.append(i)
        self.textCharList = list
        
    # Create transistion Matrix (dataframe)

    def createTranisitionDataframe(self):
        allowedChars = self.allowedChars
        textCharList = self.textCharList

        length = len(textCharList)

        trDF = pd.DataFrame(columns=allowedChars, index=allowedChars)
        trDF = trDF.astype(float)
        trDF = trDF.fillna(0.00)

        for i in range(length - 2):
            start = textCharList[i]
            to = textCharList[i+1]
            trDF[start][to] = trDF[start][to] + 1
        
        for start in allowedChars:
            trDF[start] = trDF[start] / sum(trDF[start])
        
        self.trDF = trDF

    # Function to predict next characters
    def predictChar(self, start, length,number):
        for _ in range(number):
            np.random.seed(np.random.randint(1000))
            predicted = []
            currentLetter = start
            predicted.append(currentLetter)

            for _ in range(length):
                problist = self.trDF[currentLetter].values.tolist()
                temp = np.random.choice(self.allowedChars, 1, p=problist)
                predicted.append(temp[0])
                currentLetter = temp[0]
            print(predicted)
            
text = "the quick brown fox jumped over the fox!"
# creating object of the class
mChain = markovChar(text)
# Calling conversion to character
mChain.charList()
# Calling tnx matrix creation
mChain.createTranisitionDataframe()
# Giving first letter to be 't', generating chars for length of 20, and 5 samples
mChain.predictChar('t',20,5)