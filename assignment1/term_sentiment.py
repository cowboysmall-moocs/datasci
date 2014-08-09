import sys
import json

from collections import defaultdict


def main():
    scores = {}
    with open(sys.argv[1]) as file:
        for line in file:
            term, score  = line.split("\t")
            scores[term] = int(score)

    sentiments = {}
    with open(sys.argv[2]) as file:
        for line in file:
            data = json.loads(line)
            sentiment = 0
            if 'text' in data:
                tweet = data['text']
                words = tweet.split(' ')
                for word in words:
                    word = word.lower()
                    if word in scores:
                        sentiment += scores[word]
                sentiments[tweet] = sentiment

    terms  = defaultdict(int)
    counts = defaultdict(int)
    for tweet, sentiment in sentiments.iteritems():
        words = tweet.split(' ')
        for word in words:
            word = word.lower()
            if word != '':
                terms[word]  += sentiment
                counts[word] += 1

    for term, sentiment in terms.iteritems():
        print '%s %s' % (term.encode('utf-8'), float(sentiment) / counts[term])


if __name__ == '__main__':
    main()
