import os
import math
import re

class MovieReview:
    def __init__(self, polarity, filename): 
        self.polarity = polarity
        self.filename = filename
        self.vector = {
            "awful": 0,
            "bad": 0,
            "boring": 0,
            "dull": 0,
            "effective": 0,
            "enjoyable": 0,
            "great": 0,
            "hilarious": 0
        }
        self.review = ""

        # Parse the fold number from the filename
        foldString = re.search('cv(\d+?)_', filename)
        if foldString:
            self.fold = math.floor(int(foldString.group(1)) / 100) + 1

    def parse(self):
        f = open(self.filename)
        for word in f.read().split():
            self.review += word + " "
            if word.lower() in self.vector:
                self.vector[word] = 1
    
    def predict(self):
        # Use vector to predict 
        return

    def __add__(self, other):
        combinedResult = MovieReview(self.polarity, "")
        for word in self.vector:
            combinedResult.vector[word] = self.vector[word] + other.vector[word]
        return combinedResult