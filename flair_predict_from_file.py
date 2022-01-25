from flair.data import Sentence
from flair.models import TextClassifier

classifier = TextClassifier.load('model2/final-model.pt')

test_file = 'corp1/test.txt'

cnt_total = 0
cnt_correct = 0

for line in open(test_file, 'r'):
    split = line.split(' ', 1)
    actual = split[0].replace('__label__', '')
    try:
        sentence = Sentence(split[1])
    except:
        continue
    classifier.predict(sentence)
    cnt_total += 1
    try:
        predicted = str(sentence.labels[0]).split(' ')[0]
    except:
        continue
    if predicted == actual:
        cnt_correct += 1
    if cnt_total % 1000 == 0:
        print(f'{cnt_total} {cnt_correct}')

print(cnt_total)
print(cnt_correct)
print(cnt_correct / cnt_total)

