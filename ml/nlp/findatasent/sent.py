import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import f1_score
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier



df = pd.read_csv("/Users/james04nesbitt/PycharmProjects/DS:ML/ml/nlp/findatasent/data.csv")
X,y = df['Sentence'], df['Sentiment']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=1)
i = 1
while i <=10:
    clf = SVC(C=2, kernel='sigmoid')
    count_vect = TfidfVectorizer()

    train_vect = count_vect.fit_transform(X_train)

    test_vectors = count_vect.transform(X_test)

    
    clf.fit(train_vect, y_train)

    pred = clf.predict(test_vectors)

    score = f1_score(y_test, pred, average='macro')
    print(score, i)
    
    

