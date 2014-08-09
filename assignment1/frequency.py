import sys
import json

from collections import defaultdict


def main():
    counts = defaultdict(int)
    total  = 0
    with open(sys.argv[1]) as file:
        for line in file:
            data = json.loads(line)
            if 'text' in data:
                tweet = data['text']
                words = tweet.split(' ')
                for word in words:
                    word = word.lower()
                    if word != '':
                        counts[word] += 1
                        total += 1

    for word, count in counts.iteritems():
        print '%s %s' % (word.encode('utf-8'), float(count) / total)


if __name__ == '__main__':
    main()
