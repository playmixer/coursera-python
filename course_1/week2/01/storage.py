import sys
import os
from os.path import exists
import tempfile
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("--key")
parser.add_argument("--val")
args = parser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

if exists(storage_path) == False:
    with open(storage_path, 'w') as f:
        f.close()

with open(storage_path, 'r') as f:    
    read_file = f.read() or json.dumps(dict())

    json_data = json.loads(read_file)

    if args.key not in json_data:
        json_data[args.key] = [] 

    if args.val == None:
        print(', '.join(json_data[args.key]))
    else:
        json_data[args.key].append(args.val)
    f.close()

with open(storage_path, 'w') as f:
    f.write(json.dumps(json_data))
    f.close()
