import numpy as np
import pandas as pd
from sklearn import preprocessing
from textblob.classifiers import NaiveBayesClassifier
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB

data = pd.DataFrame([
    [4., 45., 984.],
    [np.nan, np.nan, 5.],
    [94., 23., 55.],
])

data = data.fillna(data.mean()) 
print(data.fillna(0.1))
print(data)

scaled_values = preprocessing.MinMaxScaler(feature_range=(0, 1))
results       = scaled_values.fit(data).transform(data)

print(results)

stand_scaler = preprocessing.StandardScaler().fit(data)
results      = stand_scaler.transform(data)

print(results)

results = preprocessing.Binarizer(threshold=50.0).fit(data).transform(data)
print(results)

train = [
    ('I love this sandwich.', 'pos'),
    ('This is an amazing shop!', 'pos'),
    ('We feel very good about these beers.', 'pos'),
    ('That is my best sword.', 'pos'),
    ('This is an awesome post', 'pos'),
    ('I do not like this cafe', 'neg'),
    ('I am tired of this bed.', 'neg'),
    ("I can't deal with this", 'neg'),
    ('She is my sworn enemy!', 'neg'),
    ('I never had a caring mom.', 'neg')
]

c1 = NaiveBayesClassifier(train)
print(c1.classify("I just love breakfast"))
print(c1.classify("Yesterday was Sunday"))
print(c1.classify("Why can't he pay my bills"))
print(c1.classify("They want to kill the president of Bantu"))

categories    = ['alt.atheism', 'soc.religion.christian', 'comp.graphics', 'sci.med']
training_data = fetch_20newsgroups(subset='train', categories=categories, shuffle=True, random_state=42)
print(len(training_data))

print(training_data.target_names[0])

sentence_1 = "As fit as a fiddle"
sentence_2 = "As you like it"
set((sentence_1 + sentence_2).split(" "))

count_vect         = CountVectorizer()
training_matrix    = count_vect.fit_transform(training_data.data)
matrix_transformer = TfidfTransformer()
tfidf_data         = matrix_transformer.fit_transform(training_matrix)
print(tfidf_data[1:4].todense())

model       = MultinomialNB().fit(tfidf_data, training_data.target)
test_data   = ["My God is good", "Arm chip set will rival intel"]
test_counts = count_vect.transform(test_data)
new_tfidf   = matrix_transformer.transform(test_counts)
prediction  = model.predict(new_tfidf)

for doc, category in zip(test_data, prediction):
    print('%r => %s' % (doc, training_data.target_names[category]))
