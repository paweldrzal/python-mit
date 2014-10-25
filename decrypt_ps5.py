def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
	
    ### TODO
    noWords=0
    bestShift=0
    Shift=0
    while Shift<26:
        decodedMessage = applyShift(text,Shift)
        words = decodedMessage.split(" ")
        counter = 0
        for w in words:
            if isWord(wordList,w)==True:
                counter +=1
        if counter > noWords:
            noWords = counter
            bestShift = Shift
        Shift += 1
    return bestShift
	
"""
>>> s = applyShift('Hello, world!', 8)
>>> s
'Pmttw, ewztl!'
>>> findBestShift(wordList, s)
18
>>> applyShift(s, 18)
'Hello, world!'"""


def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Once you decrypt the message, be sure to include as a comment
    your decryption of the story.

    returns: string - story in plain text
    """
    ### TODO
    story = getStoryString()
    wordList = loadWords()
    return applyShift(story,findBestShift(wordList,story))

if __name__ == '__main__':
    decryptStory()