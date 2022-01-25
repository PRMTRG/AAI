"""
This script extracts (in memory) a .zst archive containing json data with 
reddit comments and saves the comments from chosen subreddits to individual
json files.
The source of the used archive is pushshift.io.
The code used for extraction is based on:
https://old.reddit.com/r/pushshift/comments/ajmcc0/information_and_code_examples_on_how_to_use_the/ef012vk/
"""

import json
import zstandard as zstd

subreddits = [
    'linux',
    'gaming',
    'politics',
    'Coronavirus',
    'AmItheAsshole',
    'wallstreetbets'
]

files = {}
for subreddit in subreddits:
    files[subreddit] = open(subreddit + '.json', 'w', encoding='utf-8')

cnt = 0
with open("./RC_2021-06.zst", 'rb') as fh:
    dctx = zstd.ZstdDecompressor(max_window_size=2147483648)
    with dctx.stream_reader(fh) as reader:
        previous_line = ""
        while True:
            chunk = reader.read(2**24)
            if not chunk:
                break
            string_data = chunk.decode('utf-8')
            lines = string_data.split("\n")
            for i, line in enumerate(lines[:-1]):
                if i == 0:
                    line = previous_line + line
                object = json.loads(line)
                for subreddit in subreddits:
                    if object['subreddit'] == subreddit:
                        files[subreddit].write(line)
                        files[subreddit].write('\n')
                cnt += 1
                if cnt % 100000 == 0:
                    print(cnt)
            previous_line = lines[-1]

for subreddit in subreddits:
    files[subreddit].close()

