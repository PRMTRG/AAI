from flair.data import Corpus
from flair.datasets import ClassificationCorpus
from flair.embeddings import WordEmbeddings, DocumentRNNEmbeddings
from flair.models import TextClassifier
from flair.trainers import ModelTrainer


data_folder = './corp2'

label_type = 'subreddit'

corpus: Corpus = ClassificationCorpus(data_folder,
                                      test_file='test.txt',
                                      dev_file='dev.txt',
                                      train_file='train.txt',                                       
                                      label_type=label_type,
                                      )
corpus = corpus.downsample(0.03)

label_dict = corpus.make_label_dictionary(label_type=label_type)

glove_embedding = WordEmbeddings('glove')

document_embeddings = DocumentRNNEmbeddings([glove_embedding])

classifier = TextClassifier(document_embeddings, label_dictionary=label_dict, label_type=label_type)

trainer = ModelTrainer(classifier, corpus)

trainer.fine_tune('model3',
                  learning_rate=5.0e-5,
                  mini_batch_size=4,
                  max_epochs=10,
                  embeddings_storage_mode='cpu',
                  checkpoint=True,
                  )

