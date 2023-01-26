import pyttsx3
import speech_recognition as sr
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
import pickle
import pandas as pd

class Reco_vocal:
    def __init__(self):
        self.speech  = sr.Recognizer()
        self.mic = sr.Microphone()
        self.av = pyttsx3.init()
        self.text_clf = Pipeline([('tfidf', TfidfVectorizer()),
                                  ('clf', LinearSVC())])
        self.X_test = None
        self.y_test = None
        self.filename = '../model/nlp_language_model.sav'
        self.loaded_model = pickle.load(open(self.filename, 'rb'))

    def train(self):
        df = pd.read_csv(
            "../data/sentence_language.csv", encoding='utf8')
        df.dropna(inplace=True)

        blanks = []
        # (index, label, sentence)
        for i, lb, sent in df.itertuples():
            if sent.isspace():
                blanks.append(i)
        df.drop(blanks, inplace=True)

        X = df['Text']
        y = df['Language']

        X_train, self.X_test, y_train, self.y_test = train_test_split(
            X, y, test_size=0.33, random_state=42)

        self.text_clf.fit(X_train, y_train)

        pickle.dump(self.text_clf, open(self.filename, 'wb'))


    def predict(self, sentence):
        return self.loaded_model.predict([sentence])

    def metrics(self):
        predictions = self.loaded_model.predict(self.X_test)
        print(confusion_matrix(self.y_test, predictions))
        print('\n\n')
        print(classification_report(self.y_test, predictions))
        print('\n\n')
        print("accuracy score: ", accuracy_score(self.y_test, predictions))

    def readText(self,text):
        self.av.say(text)
        self.av.runAndWait()

    def command(self):
        try:
            self.readText("Je suis à votre écoute.")

            with self.mic as source:
                self.speech.pause_threshold = 1
                self.speech.adjust_for_ambient_noise(source)
                audio = self.speech.listen(source)
            request = self.speech.recognize_google(audio, language='fr-FR')

            if self.loaded_model.predict([request]) == 'French':
                return request
            else :
                self.readText("Veuillez reformuler votre demande en français.")
                return None
        except Exception as e:
            self.readText("Je n'ai pas compris, pouvez vous répéter ?")
            return None