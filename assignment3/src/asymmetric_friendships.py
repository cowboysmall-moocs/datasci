import MapReduce
import sys


mr = MapReduce.MapReduce()


def mapper(record):
    mr.emit_intermediate((record[1], record[0]), 1)
    mr.emit_intermediate((record[0], record[1]), 1)


def reducer(key, list_of_values):
    if len(list_of_values) == 1:
        mr.emit(key)


def main(args):
    mr.execute(open(args[0]), mapper, reducer)


if __name__ == "__main__":
    main(sys.argv[1:])

