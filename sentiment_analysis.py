# -*- coding: utf-8 -*-


import pandas as pd

#import the dataset as a csv file
dataset = pd.read_csv('/Restaurant_Reviews.tsv', delimiter='\t',quoting=3)

dataset

#importing the nltk and re library for preprocessing and cleaning of data
import nltk
import re

#updating the stopwords in the nltk library
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

corpus = []
ps = PorterStemmer()
all_stopwords = stopwords.words('english')
all_stopwords.remove('not')

for line in range(0,1000):
  review = re.sub('[^a-zA-Z] ', ' ', dataset['Review'][line])
  review = review.lower()
  review = review.split()
  review = [ps.stem(word) for word in review if not word in set(all_stopwords)]
  review = ' '.join(review)
  corpus.append(review)

print(corpus)

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=1500)
x = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:,-1].values

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25)

y_test

x_test

x_train

y_train

from sklearn.naive_bayes import GaussianNB

gnb = GaussianNB()
gnb.fit(x_train, y_train)
y_pred = gnb.predict(x_test)

import pickle


with open('model.pkl', 'wb') as f:
    pickle.dump(gnb, f)

y_pred

from sklearn.metrics import confusion_matrix,accuracy_score
cm = confusion_matrix(y_test,y_pred)

cm

accuracy_score(y_test,y_pred)

new_review  = ['nice food buddy','it was not that good','i dont like the food','it was ok i guess','i dont know but the food seems nice and good']
test_review = cv.fit_transform(new_review).toarray()
print(test_review)

