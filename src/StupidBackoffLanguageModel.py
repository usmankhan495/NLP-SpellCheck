import collections
import math


class StupidBackoffLanguageModel:

  def __init__(self, corpus):
    """Initialize your data structures in the constructor."""
    self.unigramCounts = collections.defaultdict(lambda: 0)
    self.bigramCounts = collections.defaultdict(lambda: 0)
    self.total = 0
    self.train(corpus)

  def train(self, corpus):
    """ Takes a corpus and trains your language model. 
        Compute any counts or other corpus statistics in this function.
    """


    temp = ""
    for sentence in corpus.corpus:

      i = 0
      for datum in sentence.data:
        # print str(sentence.data)
        self.total=self.total+1
        token = datum.word
        self.unigramCounts[token] = self.unigramCounts[token] + 1
        if (i == 0):
          temp = datum.word
          i = i + 1
          continue

        i = i + 1

        key = temp + "," + token
        self.bigramCounts[key] = self.bigramCounts[key] + 1
        #  print token
        temp = token

    pass

  def score(self, sentence):
    """ Takes a list of strings as argument and returns the log-probability of the 
        sentence using your language model. Use whatever data you computed in train() here.
    """

    score = 0.0
    i = 0
    temp = ""
    for token in sentence:
      count = self.unigramCounts[token]
      if (i == 0):
        i = i + 1
        temp = token
        continue

      key = temp + "," + token
      bicount = self.bigramCounts[key]
      unicount = self.unigramCounts[temp]
      temp = token
      if bicount > 0 :

         score += (math.log(bicount) - math.log(unicount))
      else:
        unicount = self.unigramCounts[token]
        score += math.log(unicount + 1) + math.log(0.4)
        score -= math.log(self.total + len(self.unigramCounts))

    return score
