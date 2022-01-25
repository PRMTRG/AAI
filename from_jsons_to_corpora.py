"""
This script loads data from json files (each containing comments
from a chosen subreddit) and saves them to files in FastText format.
In this format each line looks as such:
__{label}__ {comment_body}

The comments are shuffled and split into three files:
80% - train.txt (training data)
10% - dev.txt (validation data)
10% - test.txt (test data) 
"""

import json
import random
import os

jsons_dir = 'jsons/'

output_dir = 'corp2/'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)
else:
    if len(os.listdir(output_dir)) != 0:
        import sys
        sys.exit('Output directory not empty')

# keys == labels
# values == paths to json files
jsons = {
    'aita': jsons_dir + 'AmItheAsshole.json',
    'politics': jsons_dir + 'politics.json',
    'linux': jsons_dir + 'linux.json',
    'wsb': jsons_dir + 'wallstreetbets.json',
}

# load comments from files into lists in the 'comments' dictionary
comments = {}
for j in jsons:
    comments[j] = []
    for line in open(jsons[j], 'r'):
        comment = json.loads(line)
        # ignore comments made by moderators
        # (they're usually made by bots)
        if comment['distinguished'] == 'moderator':
            continue
        # ignore removed/deleted comments
        if comment['body'] == '[removed]' or comment['body'] == '[deleted]':
            continue
        # remove newlines from comment body and append to list
        comments[j].append([j, comment['body'].replace('\n',' ')])

for j in jsons:
    random.shuffle(comments[j])

# remove 90% of comments from subreddits other than 'linux'
# (this one has less data overall)
for j in jsons:
    if j == 'linux':
        continue
    comments[j] = comments[j][:round(len(comments[j]) * 0.1)]

train = []
dev = []
test = []
for j in jsons:
    a = round(len(comments[j]) * 0.8)
    b = round(len(comments[j]) * 0.9)
    train += comments[j][:a]
    dev += comments[j][a:b]
    test += comments[j][b:]

random.shuffle(train)
random.shuffle(dev)
random.shuffle(test)

with open(output_dir + 'train.txt', 'w') as file:
    for el in train:
        file.write(f'__label__{el[0]} {el[1]}\n')
with open(output_dir + 'dev.txt', 'w') as file:
    for el in dev:
        file.write(f'__label__{el[0]} {el[1]}\n')
with open(output_dir + 'test.txt', 'w') as file:
    for el in test:
        file.write(f'__label__{el[0]} {el[1]}\n')

