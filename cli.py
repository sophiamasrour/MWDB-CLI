import os
import sys
import argparse
import magic
from mwdblib import MWDB


VTURL = 'https://virustotal.com/gui/file'

class CLI(MWDB):

    def __init__(self) -> None:
        super().__init__()

    def batch_upload(self, sample, tags):

        from scripts import batch_upload
        try:
            paths = batch_upload.get_samples_path(sample)
            batch_upload.upload_files(paths, tags)

        except Exception as m:
            print(f'error: {m}')
    
    def batch_reanalysis(self, sample):

        from scripts import batch_reanalysis
        batch_reanalysis.query_and_reanalyze(sample)
    
    def last_two(self, hash):
        from scripts import last_two
        print(last_two.last_two_karton(hash))


        


parser = argparse.ArgumentParser(
    description='MWDB CLI',
    add_help=True
)

parser.add_argument('-u', nargs='+', help='Upload sample')
parser.add_argument('-r', nargs=1, help='Run full reanalysis on all matched samples')
parser.add_argument('--last-two', nargs='+', type=str, help=' Retrieve results from the latest two Karton analyses instead of one')

args = parser.parse_args()

if __name__ == '__main__':
    cli = CLI()
    if args.u:
        tags = args.u[1:]
        cli.batch_upload(args.u[0], tags)

    elif args.r:
        cli.batch_reanalysis(args.r[0])

    elif args.last_two:
        cli.last_two(args.last_two[0])
