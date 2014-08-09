import MapReduce
import sys


mr = MapReduce.MapReduce()


def mapper(record):
    mr.emit_intermediate(record[1], record)


def reducer(key, list_of_values):
    order = list_of_values[0]
    for line_item in list_of_values[1:]:
        mr.emit(order + line_item)


def main(args):
    mr.execute(open(args[0]), mapper, reducer)


if __name__ == "__main__":
    main(sys.argv[1:])

