import pickle
import os
import nltk
from nltk.corpus import stopwords
from nltk.stem.lancaster import LancasterStemmer


class PredictionService:
    def __init__(self):
        self.load_model()
        self.load_nltk()

    def predict(self, data):
        pass

    def load_model(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        MODEL_PATH = os.path.join(
            BASE_DIR, "..", "trained_models", "sa_classifier.pickle"
        )

        try:
            with open(MODEL_PATH, "rb") as file:
                model = pickle.load(file)
            self.model = model
        except FileNotFoundError:
            print(f"Model file not found: {MODEL_PATH}")
            return None
        except Exception as e:
            print(f"Error loading model: {e}")
            return None

    def load_nltk(self):
        nltk.download("punkt")
        nltk.download("stopwords")

        self.stopword_list = stopwords.words("english")
        self.stemmer = LancasterStemmer()
