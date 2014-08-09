import sys
import json

from collections import defaultdict


def main():
    hashtag_counts = defaultdict(int)
    total  = 0
    with open(sys.argv[1]) as file:
        for line in file:
            data = json.loads(line)
            if 'entities' in data:
                entities = data['entities']
                if 'hashtags' in entities:
                    hashtags = entities['hashtags']
                    for hashtag in hashtags:
                        text = hashtag['text'].lower()
                        hashtag_counts[text] += 1

    counts_hashtag = sorted([(value, text) for text, value in hashtag_counts.iteritems()], reverse = True)

    for count, hashtag in counts_hashtag[0:10]:
        print '%s %s' % (hashtag.encode('utf-8'), count)


if __name__ == '__main__':
    main()
