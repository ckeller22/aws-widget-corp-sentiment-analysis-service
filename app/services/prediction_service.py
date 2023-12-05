import pickle
import os


class PredictionService:
    def __init__(self):
        self.model = self.load_model()

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
            return model
        except FileNotFoundError:
            print(f"Model file not found: {MODEL_PATH}")
            return None
        except Exception as e:
            print(f"Error loading model: {e}")
            return None
