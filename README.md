
#Prerequisite
pipenv needs to be setup to run this project, [setup pipenv](https://pipenv.pypa.io/en/latest/)

Once pipenv is setup you need to run `pipenv shell` to start the virtual env

#Download dataset

To download the dataset run `python download_dataset.py`
It should have downloaded it in the root folder and unzipped it in `dataset_out`

# Query database

To Query the database

`python rundb.py --query_json <json_string>`

eg:
`python rundb.py --query_json "{\"breeds\": [\"Calico\", \"Siamese\"], \"age_low\": -13, \"age_high\": 444}"`

