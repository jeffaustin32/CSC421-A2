import random
from movieReview import MovieReview
from classifier import Classifier
import numpy as np


# Load all the training data from files
classifier = Classifier()
classifier.loadTrainingData("pos", "pos")
classifier.loadTrainingData("neg", "neg")

# Train on all data,calculate probabilites, and accuracy
print("Training on all data ==========")
classifier.train(["pos", "neg"])
print(classifier.probabilities)
print(classifier.getConfusionMatrix())

print("\nk-fold training ==========")
# Perform k-fold to get less fitted probabilities
classifier.kFold(10, ["pos", "neg"])


# Train on all data,calculate probabilites, and accuracy
print(classifier.probabilities)
print(classifier.getConfusionMatrix())


print(classifier.generateReview("pos"))
print(classifier.generateReview("pos"))
print(classifier.generateReview("pos"))
print(classifier.generateReview("pos"))
print(classifier.generateReview("pos"))

print(classifier.generateReview("neg"))
print(classifier.generateReview("neg"))
print(classifier.generateReview("neg"))
print(classifier.generateReview("neg"))
print(classifier.generateReview("neg"))