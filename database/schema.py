import json
import os.path
from dataclasses import dataclass, asdict


@dataclass
class Pet:
    pet_id: str = None
    pet_type: str = None
    name: str = None
    age: int = None
    breed: str = None
    color: str = None
    fur_length: str = None
    vaccinated: str = None
    gender: int = None
    entry_date: str = None
    story: str = None
    owner_location_id: int = None
    owner_account_id: str = None
    owner: str = None
    prefix_path: str = None

    def image_path(self):
        return os.path.join(self.prefix_path, f"pet-{self.pet_id}.jpg")

    def __repr__(self):
        out = asdict(self)
        out["image_path"] = self.image_path()
        return str(out)

    def __cmp__(self, other):
        return self.age.__cmp__(other.age)

    def __lt__(self, other):
        if isinstance(other, Pet):
            return self.age < other.age
        elif isinstance(other, int):
            return self.age < other

    def __gt__(self, other):
        if isinstance(other, Pet):
            return self.age > other.age
        elif isinstance(other, int):
            return self.age > other
