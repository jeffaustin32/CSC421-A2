import random
import os
import functools
from movieReview import MovieReview

class Classifier:
    def __init__(self):
        self.probabilities = dict()
        self.reviews = []

    def loadTrainingData(self, directory, label):
        # Open and parse every review in the directory
        for filename in os.listdir(os.getcwd() + "/" + directory):
            movieReview = MovieReview(directory, os.getcwd() + "/" + directory + "/" + filename)
            movieReview.parse()
            self.reviews.append(movieReview)

    def train(self, polarities, testFold=0):
        for polarity in polarities:
            # Filter the reviews to train on to only those with
            # the correct polarity and not part of the test fold
            filteredReviews = list(filter(lambda review: review.polarity == polarity and not review.fold == testFold, self.reviews))

            # Reduce all filtered reviews
            self.probabilities[polarity] = functools.reduce(
                lambda x, y: x + y, filteredReviews).vector

            # Convert binary frequency into probability
            for wordFrequency in self.probabilities[polarity]:
                self.probabilities[polarity][wordFrequency] = self.probabilities[polarity][wordFrequency] / len(filteredReviews)
        
        return self.probabilities

    def predict(self, review):
        predictions = dict()

        # Determine likelihood for all labels trained on
        for label in self.probabilities:
            predictions[label] = self.likelihood(review, self.probabilities[label])

        # Find and return the most likely label for this review
        prediction = max(predictions.keys(), key=(lambda k: predictions[k]))
        return prediction

    def likelihood(self, review, probabilityVector):
        probabilityProduct = 1.0
        
        # For every word used in training
        for label in review.vector:
            # Determine if the word is found in the review
            if review.vector[label] == 1:
                # If so, use the probability in product calculation
                probability = probabilityVector[label]
            else:
                # If not, use the compliment of the probability
                probability = 1.0 - probabilityVector[label]
            # Take the product of all probabilities
            probabilityProduct *= probability

        return probabilityProduct

    def kFold(self, folds, labels):
        # Perform kFold on each label
        for label in labels:
            # Train this label multiple times
            foldProbabilities = []
            for i in range(folds):
                self.train([label], i)
                foldSet = self.probabilities
                foldProbabilities.append(foldSet[label])

            # Reset probabilities for this label
            self.probabilities[label] = dict()

            # Average the probabilities across each training set
            for fold in foldProbabilities:
                for word in fold:
                    if word in foldProbabilities:   
                        self.probabilities[label][word] += fold[word]
                    else:
                        self.probabilities[label][word] = fold[word]
    
    def getConfusionMatrix(self):
        confusionMatrix = [[0, 0], [0, 0]]
        for review in self.reviews:
            prediction = self.predict(review)

            if review.polarity == "pos" and prediction == "pos":
                confusionMatrix[0][0] += 1
            elif review.polarity == "pos" and prediction == "neg":
                confusionMatrix[0][1] += 1
            elif review.polarity == "neg" and prediction == "pos":
                confusionMatrix[1][0] += 1
            elif review.polarity == "neg" and prediction == "neg":
                confusionMatrix[1][1] += 1

        return confusionMatrix
    
    def generateReview(self, polarity):
        review = []
        for word in self.probabilities[polarity]:
            if self.probabilities[polarity][word] >= random.random():
                review.append(word)
        return review
