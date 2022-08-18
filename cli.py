import os
import sys
import argparse
import magic
from mwdblib import MWDB

class CLI(MWDB):

    def batch_upload(self, tags, path=''):

        from scripts import batch_upload
        try:
            paths = batch_upload.get_samples_path(path)
            print(len(paths))
            for each in paths:
                print(each)
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
parser.add_argument('--query', nargs=1, help='Lucene query')
parser.add_argument('--dirr', nargs=1, help='Path to directory of samples to be uploaded')

args = parser.parse_args()

if __name__ == '__main__':
    cli = CLI()
    if args.u:
        if args.dirr:
            cli.batch_upload(args.u[0], args.dirr[0])
        else:
            cli.batch_upload(args.u[0])

 
    elif args.r:
        cli.batch_reanalysis(args.r[0])

    elif args.last_two:
        cli.last_two(args.last_two[0])
    
    elif args.query:
        object = cli.query(args.query[0])
        print(object.data)
