#!/user/bin/env python3

import sys
from mwdblib import MWDB

def only_bsu(bsu_name: str):
    mwdb = MWDB()
    results = mwdb.search_files(f'tag:"bsu:{bsu_name}"')

    for file in results:
        print(file.file_name, end = '\n')
            
def only_capa(capa_rule: str):
    mwdb = MWDB()
    results =  mwdb.search_files(f'tag:"capa:{capa_rule}"')

    for file in results:
        print(file.file_name, end = '\n')
            
 
def bsu_and_capa(bsu_name: str, capa_rule: str):
    mwdb = MWDB()

    results =  mwdb.search_files(f'tag:"bsu:{bsu_name}" AND tag:"capa:{capa_rule}"')

    for file in results:
        print(file.file_name, end = '\n')
 
if __name__ == '__main__':
    if len(sys.argv) != 3 and len(sys.argv) != 4:
        sys.exit(f'usage: {sys.argv[0]} <b, c, or bc> <bsu name> and/or <capa rule name>')
 
    if sys.argv[1] == 'b':
        only_bsu(sys.argv[2])
    elif sys.argv[1] == 'c':
        only_capa(sys.argv[2])
    else:
        bsu_and_capa(sys.argv[2], sys.argv[3])
   
 
