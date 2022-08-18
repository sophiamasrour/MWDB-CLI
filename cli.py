import os
import sys
import argparse
import magic
from mwdblib import MWDB

class CLI(MWDB):

    def batch_upload(self, tags, path=''):

        from scripts import batch_upload
        try:
            #print('path: ' + path)
            paths = batch_upload.get_samples_path(path)
            print(len(paths))
            for each in paths:
                print(each)
            #print('tags: ' + tags)
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
    cli = CLI(api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJsb2dpbiI6InNvcGhpYSIsImFwaV9rZXlfaWQiOiIwOTA4MzI2MS00NDhmLTQwOWItYjc5MS1hNDhjODBmYjZiYmIiLCJpYXQiOjE2NTc3Mjg4NDIsImF1ZCI6Imh0dHA6Ly8wLjAuMC4wOjUwMDAiLCJzY29wZSI6ImFwaV9rZXkiLCJzdWIiOiJzb3BoaWEifQ.HsmGFocjW-wVOWGXMngzIoY5pzfNP4DBFebfu_i7a4vewFtHOG7CeboLNrrjNqBecJlUg3yGOEMTx8bDu3NxkQ', api_url = 'https://mwdb-development.labs:5000/api/', verify_ssl = False)
    if args.u:
        if args.dirr:
            #print('dir: ' + args.dirr[0])
            #print('name: ' + args.u[0])
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
