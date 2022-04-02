import urllib.request as req
import shutil
import os

import progressbar
import urllib.request


pbar = None

# https://stackoverflow.com/questions/37748105/how-to-use-progressbar-module-with-urlretrieve
def show_progress(block_num, block_size, total_size):
    global pbar
    if pbar is None:
        pbar = progressbar.ProgressBar(maxval=total_size)
        pbar.start()

    downloaded = block_num * block_size
    if downloaded < total_size:
        pbar.update(downloaded)
    else:
        pbar.finish()
        pbar = None

def get_dataset_from_url():
    """
    Utility function to download dataset
    :return: None
    """
    if not os.path.isfile("./sweepstakes_sample.zip"):
        req.urlretrieve("https://pets-challenge.s3.eu-central-1.amazonaws.com/sweepstakes_sample.zip",
                        "./sweepstakes_sample.zip", show_progress)


if __name__ == '__main__':
    get_dataset_from_url()
    if os.path.exists("./dataset_out"):
        shutil.rmtree("./dataset_out")
    shutil.unpack_archive("./sweepstakes_sample.zip", "./dataset_out")
