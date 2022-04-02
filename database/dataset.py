import glob
import json
import os
from typing import Dict
# https://docs.python.org/3/library/bisect.html#searching-sorted-lists
import bisect
import sortedcollections
import pathlib

from database.schema import Pet


def convert_db_result_to_list(db: Dict[str, list]):
    result = []
    for key in db:
        result += db[key]
    return result


class Dataset:
    """
    Analogous to sparks dataset

    """

    def __init__(self, path: str):
        self.path = path
        self.db: Dict[str, sortedcollections.SortedList] = {}

    def read_data(self):
        for file in glob.glob(os.path.join(self.path, '*.json')):
            with open(file) as fh:
                file_content = json.load(fh)
                for obj in file_content:
                    image_paths = os.path.join(pathlib.Path(self.path).parent, "imgs")
                    pet = Pet(**obj, prefix_path=image_paths)
                    if pet.breed in self.db:
                        self.db[pet.breed].add(pet)
                    else:
                        self.db[pet.breed] = sortedcollections.SortedList([pet])

    def query_by_breeds(self, breeds: list[str]):
        if breeds is not None:
            breeds_unique = set(breeds)
            breed_result = {breed: self.db[breed] for breed in breeds_unique}
        else:
            breed_result = self.db
        return breed_result

    def query(self, breeds: list[str], age_low: int, age_high: int):
        breed_result = self.query_by_breeds(breeds)
        for breed in breed_result:
            idx_low = breed_result[breed].bisect_left(age_low)
            idx_high = breed_result[breed].bisect_right(age_high)
            breed_result[breed] = breed_result[breed][idx_low: idx_high]
        return convert_db_result_to_list(breed_result)
