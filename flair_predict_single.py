from flair.data import Sentence
from flair.models import TextClassifier


classifier = TextClassifier.load('model2/final-model.pt')

text = """Maybe i am being optimistic, but i think the simple fact that Nancy Pelosi was against it could get enough republicans on board to make this actually possible."""

sentence = Sentence(text)
classifier.predict(sentence)
print(sentence.labels)


