import MapReduce
import sys


mr = MapReduce.MapReduce()


def mapper(record):
    m = record[0]
    r = record[1]
    c = record[2]
    v = record[3]
    if m == 'a':
        for k in range(5):
            mr.emit_intermediate((r, k), (c, v))
    else:
        for k in range(5):
            mr.emit_intermediate((k, c), (r, v))


def reducer(key, list_of_values):
    total = 0
    for i in range(5):
        filtered = [t[1] for t in list_of_values if t[0] == i]
        if len(filtered) == 2:
            total += (filtered[0] * filtered[1])

    mr.emit((key[0], key[1], total))


def main(args):
    mr.execute(open(args[0]), mapper, reducer)


if __name__ == "__main__":
    main(sys.argv[1:])

