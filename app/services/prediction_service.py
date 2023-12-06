import pickle
import os
import nltk
from nltk.corpus import stopwords
from nltk.stem.lancaster import LancasterStemmer
from nltk import everygrams
from string import punctuation as punctuation_list
from nltk.tokenize import word_tokenize


class PredictionService:
    def __init__(self):
        self.load_model()
        self.load_nltk()

    def get_sentiment(self, input_string):
        words = self.extract_features(input_string)
        words = self.bag_of_words(words)
        return self.model.classify(words)

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

    def extract_features(self, input_string):
        """Extract features from the input string for sentiment analysis."""
        # Tokenize words.
        words = word_tokenize(input_string)

        # Second pass, remove stop words and punctuation.
        features = [
            self.stemmer.stem(word)
            for word in words
            if self.stemmer.stem(word) not in self.stopword_list
            and self.stemmer.stem(word) not in punctuation_list
        ]

        # Third pass, generate n_grams
        n_grams = everygrams(features, max_len=3)

        return n_grams

    def bag_of_words(self, words):
        """Create a bag of words from the input words."""
        bag = {}
        for word in words:
            bag[word] = bag.get(word, 0) + 1
        return bag
