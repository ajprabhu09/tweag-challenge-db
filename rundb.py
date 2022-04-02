import json

from dask.distributed import Client, progress
from database.dataset import Dataset
import pprint
import argparse
if __name__ == '__main__':
    x = Dataset("dataset_out/sweepstakes_sample/entries")
    # client = Client(processes=False, threads_per_worker=4,
    #                 n_workers=1, memory_limit='2GB')
    # client
    x.read_data()
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--query_json', type=str,
                        help='an integer for the accumulator', required=True)

    args = parser.parse_args()
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(x.query(**json.loads(args.query_json)))