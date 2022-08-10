#!/usr/bin/env python3

import sys
from mwdblib import MWDB

def last_two_karton(hash: str):
    mwdb = MWDB()
    file = mwdb.query_file(hash)

    try:
        karton_id_0 = file.metakeys["karton"][-1]
        karton_id_1 = file.metakeys["karton"][-2]
    except IndexError:
        raise

    return karton_id_0, karton_id_1
    


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(f'usage: {sys.argv[0]} <hash>')
    
    print(last_two_karton(sys.argv[1]))
 
   
   

