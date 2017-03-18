import collections
import math


class CustomLanguageModel:
    def __init__(self, corpus):
        """Initialize your data structures in the constructor."""
        self.unigramCounts = collections.defaultdict(lambda: 0)
        self.bigramCounts = collections.defaultdict(lambda: 0)
        self.trigramCounts = collections.defaultdict(lambda: 0)

        self.total = 0
        self.train(corpus)


    def train(self, corpus):
        temp1 = ""
        temp2 = ""


        for sentence in corpus.corpus:

            i = 0
            for datum in sentence.data:
               # print str(sentence.data)
              self.total = self.total + 1
              token = datum.word
              self.unigramCounts[token] = self.unigramCounts[token] + 1
              if (i == 0):
                 temp1 = datum.word
                 i = i + 1
                 continue
              if i == 1:
                temp2 = datum.word
                i = i + 1
                continue

              i = i + 1

              key = temp1 + ","+temp2 + "," + token
              key2 = temp2 + "," + token
              self.trigramCounts[key] = self.trigramCounts[key] + 1
              self.bigramCounts[key2] = self.bigramCounts[key2] + 1
              temp1=temp2
              temp2=token








    def score(self, sentence):


         score = 0.0
         i = 0
         temp1 = ""
         temp2 = ""


         for token in sentence:
            count = self.unigramCounts[token]
            if (i == 0):
              i = i + 1
              temp1 = token
              continue
            if (i == 1):
               i = i + 1
               temp2 = token
               continue

            key = temp1 + ","+temp2 + "," + token
            key2 = temp2 + "," + token
            tricount = self.trigramCounts[key]
            bicount = self.bigramCounts[key2]
            temp = token
            if tricount > 0:
              score += math.log(tricount)
              score -= math.log(bicount)

            elif bicount > 0:
             score += math.log(0.4) + math.log(bicount)
             score -= math.log(self.unigramCounts[temp2])
            else:
             score += math.log(0.4) + math.log(self.unigramCounts[token] + 1)
             score -= math.log(self.total + (len(self.unigramCounts)))

            temp1=temp2
            temp2=token

         return score
