# AAI
This project attempts to use NLP to perform classification of reddit comments, predicting which subreddit they were posted in. 

## Setting up a local Python environment
1. Install [conda](https://docs.conda.io/en/latest/).
2. Create and activate the conda environment.
3. Install [pytorch](https://pytorch.org/get-started/locally/), e.g.:
```conda install pytorch torchvision torchaudio cpuonly -c pytorch```
4. Install flair:
```pip install flair```
 
## Usage
- from_archive_to_jsons.py - save comments from chosen subreddits to individual json files
- from_jsons_to_corpora.py - create fastText format files which will later be loaded by flair
- flair_train.py - train a model using Recursive Neural Network document embeddings
- colab_aai_projekt.py - meant for use on Google Colab - load corpus data from Google Drive and train models using Transformer document embeddings
- flair_predict_single.py - perform prediction on a single comment
- flair_predict_from_file.py - perform prediction on comments in a fastText format file

