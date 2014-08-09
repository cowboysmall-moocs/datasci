import MapReduce
import sys


mr = MapReduce.MapReduce()


def mapper(record):
    nucleotides = record[1][:-10]
    mr.emit_intermediate(nucleotides, 1)


def reducer(key, list_of_values):
    mr.emit(key)


def main(args):
    mr.execute(open(args[0]), mapper, reducer)


if __name__ == "__main__":
    main(sys.argv[1:])

