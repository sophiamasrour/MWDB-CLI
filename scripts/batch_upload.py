#!/usr/bin/env python3
import os
import sys

import magic
from mwdblib import MWDB

VTURL = 'https://virustotal.com/gui/file'


def make_virustotal_link(shasum: str):
    return VTURL + '/' + shasum


def file_wanted(path: str):
    mime = magic.from_file(path, mime=True)
    return mime == 'application/x-dosexec'


def get_file_content(file_path: str):
    with open(file_path, 'rb') as f:
        data = f.read()
    return data


def get_samples_path(dir_path: str):
    ret = []
    for (root, dirnames, filenames) in os.walk(dir_path):
        if root == dir_path:
            for name in filenames:
                full_path = os.path.join(root, name)
                if file_wanted(full_path):
                    ret.append((name, full_path))
                else:
                    print(f'Discarding {name}')
    return ret


def upload_files(samples, tags):
    mwdb = MWDB()
    for (name, full) in samples:
        print(f'Uploading {full} ({magic.from_file(full, mime=True)})... ', end='')
        data = get_file_content(full)
        file_obj = mwdb.upload_file(
                name,
                data,
        )
        vt_link = make_virustotal_link(file_obj.sha256)
        file_obj.add_metakey('virustotal_link', vt_link)

        print('OK')
        for tag in tags:
            print(f'Tagging "{name}" with "{tag}"')
            file_obj.add_tag(tag)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(f'usage: {sys.argv[0]} </path/to/directory> [tag0] [tag1] ...')

    try:
        paths = get_samples_path(sys.argv[1])
        tags = sys.argv[2:]
        upload_files(paths, tags)

    except Exception as m:
        print(f'error: {m}')
