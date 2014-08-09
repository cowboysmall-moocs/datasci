import sys
import json


def main():
    scores = {}
    with open(sys.argv[1]) as file:
        for line in file:
            term, score  = line.split("\t")
            scores[term] = int(score)

    with open(sys.argv[2]) as file:
        for line in file:
            data = json.loads(line)
            sentiment = 0
            if 'text' in data:
                words = data['text'].split(' ')
                for word in words:
                    word = word.lower()
                    if word in scores:
                        sentiment += scores[word]
            print sentiment


if __name__ == '__main__':
    main()
