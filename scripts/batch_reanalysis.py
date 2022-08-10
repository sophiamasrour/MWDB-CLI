#!/usr/bin/env python3
import sys

from mwdblib import MWDB


def query_and_reanalyze(tag: str):
    mwdb = MWDB()
    query = f'tag:"{tag}"'
    print(f'[dbg] {mwdb.count(query)} files matched the tag {tag}')
    result = mwdb.search(query)
    for sample in result:
        print(f'Submitting {sample.file_name} {sample.id} for reanalysis')
        sample.reanalyze()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(f'usage: {sys.argv[0]} <tag>')

    query_and_reanalyze(sys.argv[1])
