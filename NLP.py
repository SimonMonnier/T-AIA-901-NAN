import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
import pickle
import spacy


class NLP:

    def __init__(self) -> None:
        self.text_clf = Pipeline([('tfidf', TfidfVectorizer()),
                                  ('clf', LinearSVC())])
        self.X_test = None
        self.filename = 'model/nlp_command_model.sav'
        self.nlp = spacy.load('fr_core_news_lg')


    def train(self):
        df = pd.read_csv(
            "data/data_sentence_train.csv")
        df.dropna(inplace=True)

        blanks = []
        # (index, label, sentence)
        for i, lb, sent in df.itertuples():
            if sent.isspace():
                blanks.append(i)
        df.drop(blanks, inplace=True)

        X = df['sentence']
        y = df['label']

        X_train, self.X_test, y_train, self.y_test = train_test_split(
            X, y, test_size=0.33, random_state=42)

        self.text_clf.fit(X_train, y_train)

        pickle.dump(self.text_clf, open(self.filename, 'wb'))


    def predict(self, sentence):
        loaded_model = pickle.load(open(self.filename, 'rb'))
        return loaded_model.predict([sentence])

    def metrics(self):
        loaded_model = pickle.load(open(self.filename, 'rb'))
        predictions = loaded_model.predict(self.X_test)
        df = pd.DataFrame(confusion_matrix(self.y_test, predictions), index=[
                          'not_command', 'command'], columns=['not_command', 'command'])
        print(df)
        print('\n\n')
        print(classification_report(self.y_test, predictions))
        print('\n\n')
        print("accuracy score: ", accuracy_score(self.y_test, predictions))

    def extract_location(self, sentence):
        doc = self.nlp(sentence)
        locations = []
        if doc.ents:
            for ent in doc.ents:
                locations.append(ent.text)
            if len(locations == 2):
                return locations
            else:
                return None
        else:
            return None