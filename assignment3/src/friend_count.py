import MapReduce
import sys


mr = MapReduce.MapReduce()


def mapper(record):
    mr.emit_intermediate(record[0], 1)


def reducer(key, list_of_values):
    count = 0
    for value in list_of_values:
        count += value
    mr.emit((key, count))


def main(args):
    mr.execute(open(args[0]), mapper, reducer)


if __name__ == "__main__":
    main(sys.argv[1:])

