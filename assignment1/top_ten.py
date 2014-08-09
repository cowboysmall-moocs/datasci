import sys
import json

from collections import defaultdict



def count_by_hashtag(lines):
    hashtag_counts = defaultdict(int)

    for data in lines:
        if 'entities' in data:
            entities = data['entities']
            if 'hashtags' in entities:
                for hashtag in entities['hashtags']:
                    text = hashtag['text'].lower()
                    hashtag_counts[text] += 1

    return hashtag_counts



def main(argv):
    lines = []

    with open(argv[0]) as file:
        for line in file:
            lines.append(json.loads(line))

    hashtag_counts = count_by_hashtag(lines)
    counts_hashtag = sorted([(value, text) for text, value in hashtag_counts.iteritems()], reverse = True)

    for count, hashtag in counts_hashtag[0:10]:
        print '%s %s' % (hashtag.encode('utf-8'), count)


if __name__ == '__main__':
    main(sys.argv[1:])
