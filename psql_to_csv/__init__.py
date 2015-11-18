"""psql_to_csv: when you forget to properly format the results of a query that takes forever

Usage:
  psql_to_csv [options] [-]

Options:
  -i FILE       Input File (instead of stdin)
  -o FILE       Output File (instead of stdout)
  -d delimiter  Delimter [default: \t]
"""

import sys
import csv
import re

from docopt import docopt


def parse_line(l):
    row = l.split(' |')
    return [r.strip() for r in row]


def trim_trailing_rows(rows):
    r = re.compile('^\(.*row[s]?\)')
    rows = [row for row in rows if any(row) and not r.match(row[0])]
    return rows


def parse_file(f):
    rows = [parse_line(line) for line in f]
    fieldnames = rows[0]
    rows = rows[2:]
    rows = trim_trailing_rows(rows)
    values = [{k: v for k, v in zip(fieldnames, row)}for row in rows]
    return fieldnames, values


def create_csv(f, fieldnames, values, delimiter):
    writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=delimiter)
    writer.writeheader()
    for value in values:
        writer.writerow(value)


def main():
    args = docopt(__doc__, version='psql_to_csv 0.1')
    delimiter = args['-d']
    infile = args['-i']
    outfile = args['-o']
    if infile:
        with open(infile, 'r') as f:
            fieldnames, values = parse_file(f)
    else:
        with sys.stdin as f:
            fieldnames, values = parse_file(f)
    if outfile:
        with open(outfile, 'w') as f:
            create_csv(f, fieldnames, values, delimiter=delimiter)
    else:
        with sys.stdout as f:
            create_csv(f, fieldnames, values, delimiter=delimiter)

if __name__ == "__main__":
    main()
