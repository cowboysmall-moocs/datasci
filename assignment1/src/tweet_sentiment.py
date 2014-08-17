import sys
import json



def load_scores(filepath):
    scores = {}

    with open(filepath) as file:
        for line in file:
            term, score  = line.split("\t")
            scores[term] = int(score)

    return scores



def sentiment_by_tweet(lines, scores):
    sentiments = {}

    for data in lines:
        if 'text' in data:
            sentiment = 0
            tweet = data['text']
            for word in tweet.split(' '):
                word = word.lower()
                if word in scores:
                    sentiment += scores[word]
            sentiments[tweet] = sentiment

    return sentiments



def main(argv):
    lines = []

    with open(argv[1]) as file:
        for line in file:
            lines.append(json.loads(line))

    scores     = load_scores(argv[0])
    sentiments = sentiment_by_tweet(lines, scores)

    # for tweet, sentiment in sentiments.iteritems():
    #     print '%s %s' % (tweet.encode('utf-8'), sentiment)

    for sentiment in sentiments.values():
        print sentiment



if __name__ == '__main__':
    main(sys.argv[1:])
