import MapReduce
import sys


mr = MapReduce.MapReduce()


def mapper(record):
    words = record[1].split()
    for word in words:
        mr.emit_intermediate(word, record[0])


def reducer(key, list_of_values):
    values = []
    for value in list_of_values:
        if value not in values:
            values.append(value)
    mr.emit((key, values))


def main(args):
    mr.execute(open(args[0]), mapper, reducer)


if __name__ == "__main__":
    main(sys.argv[1:])

