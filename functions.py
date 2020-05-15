"""
# Evaluation module for Conversational AI
# Lower score is better. maybe from 0 to 10?
# input for all functions: list of utternces
# output for all functions: numerical score
"""


def evalTopic(listOfUtterance):
    """
    # do something with listOfUtterance
    # find a natural language library API that returns the topic
    # maybe use word embeddings (word2vec) and calculate distance
      between topics to determine score
    """
    pass

def evalPoliteness(listOfUtterance):
    """
    # do something with listOfUtterance
    # look for words that sound mean
    # increase score whenever you find mean words
    # note: there are language models that determine the
      toxidity of a sentence
    """
    pass

def evalInteresting(listOfUtterance):
    """
    # do something with listOfUtterance
    # if it repeats a lot of the same words, then increase score
    """
    pass

def evalConsistency(listOfUtterance):
    """
    # do something with listOfUtterance
    # ????
    # create output score
    """
    pass

def evalGrammar(listOfUtterance):
    """
    # do something with listOfUtterance
    # probably there is a model that checks grammar, or an API
    # create output score
    """
    pass
