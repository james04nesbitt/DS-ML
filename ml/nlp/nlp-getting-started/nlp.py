
import pandas as pd
import numpy as np
from sklearn import feature_extraction, linear_model, model_selection, preprocessing, svm


test_df = pd.read_csv("/Users/james04nesbitt/PycharmProjects/datasciencepractice/ml/nlp/nlp-getting-started/test.csv")
train_df = pd.read_csv("/Users/james04nesbitt/PycharmProjects/datasciencepractice/ml/nlp/nlp-getting-started/train.csv")

count_vect = feature_extraction.text.CountVectorizer()

train_vect = count_vect.fit_transform(train_df["text"])

test_vectors = count_vect.transform(test_df['text'])

clf = svm.SVC(C = 1.8)
clf.fit(train_vect, train_df["target"])

test= pd.read_csv("/Users/james04nesbitt/PycharmProjects/datasciencepractice/ml/nlp/nlp-getting-started/sample_submission.csv")
test["target"] = clf.predict(test_vectors)
test.to_csv("submission.csv", index=False)

   

#C =1.8 0.6515745928389994