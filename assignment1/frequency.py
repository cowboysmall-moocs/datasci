import sys
import json

from collections import defaultdict



def frequency(lines):
    total  = 0
    counts = defaultdict(int)

    for data in lines:
        if 'text' in data:
            for word in data['text'].split(' '):
                word = word.lower()
                if word != '':
                    counts[word] += 1
                    total += 1

    return (total, counts)



def main(argv):
    lines = []

    with open(argv[0]) as file:
        for line in file:
            lines.append(json.loads(line))

    total, counts = frequency(lines)

    for word, count in counts.iteritems():
        print '%s %s' % (word.encode('utf-8'), float(count) / total)



if __name__ == '__main__':
    main(sys.argv[1:])
