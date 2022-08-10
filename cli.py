import os
import sys
import argparse

parser = argparse.ArgumentParser(
    description='MWDB CLI',
    add_help=True
)

parser.add_argument('-u', nargs='+', help='Upload sample')
parser.add_argument('-r', help='Run full reanalysis on all matched samples', action="store_true")
parser.add_argument('--last-two', nargs='+', type=str, help=' Retrieve results from the latest two Karton analyses instead of one')

args = parser.parse_args()

if __name__ == '__main__':
    if args.u:
        from scripts import batch_upload
        try:
            paths = batch_upload.get_samples_path(args.u[0])
            tags = args.u[1:]
            batch_upload.upload_files(paths, tags)

        except Exception as m:
            print(f'error: {m}')
    elif args.r:
        from scripts import batch_reanalysis
        batch_reanalysis.query_and_reanalyze(args.r[0])
    
    elif args.u:
        from scripts import last_two
        print(last_two.last_two_karton(args.u[0]))
    
    elif args.last_two:
        from scripts import last_two
        print(last_two.last_two_karton(args.last_two[0]))
