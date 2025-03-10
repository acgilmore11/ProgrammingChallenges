# CSV Combiner - Austin Gilmore Solution

## Virtual Environment Setup
This script utilizes open source [pandas](https://pandas.pydata.org/docs/) library for csv manipulation. To avoid installing package globally, a virtual environment should be used.

1. Create virtual environment using [virtualenv](https://virtualenv.pypa.io/en/latest/) CLI tool.

```
$ virtualenv venv
```

2. Activate virtual environment.

```
$ ./venv/Scripts/activate
```

3. Install required dependencies.

```
$ pip install -r requirements.txt
```

## Execution Instructions
*Before executing, ensure csv-combiner folder is current working directory (ex. /path/to/dir/ProgrammingChallenges/csv-combiner) and virtual environment is activated.

To combine multiple csv files and output to stdout:

```
$ python ./csv_combiner.py ./fixtures/accessories.csv ./fixtures/clothing.csv
```

To combine multiple csv files and redirect output to new csv file:

```
$ python ./csv_combiner.py ./fixtures/accessories.csv ./fixtures/clothing.csv > combined.csv
```

To run unit tests:

```
$ python ./combiner_test.py
```

# Original Prompt
Write a command line program that takes several CSV files as arguments. Each CSV
file (found in the `fixtures` directory of this repo) will have the same
columns. Your script should output a new CSV file to `stdout` that contains the
rows from each of the inputs along with an additional column that has the
filename from which the row came (only the file's basename, not the entire path).
Use `filename` as the header for the additional column.

##  Considerations
* You should use coding best practices. Your code should be re-usable and extensible.
* Your code should be testable by a CI/CD process. 
* Unit tests should be included.

## Example
This example is provided as one of the ways your code should run. It should also be
able to handle more than two inputs, inputs with different columns, and very large (> 2GB) 
files gracefully.

```
$ ./csv-combiner.php ./fixtures/accessories.csv ./fixtures/clothing.csv > combined.csv
```

Given two input files named `clothing.csv` and `accessories.csv`.

|email_hash|category|
|----------|--------|
|21d56b6a011f91f4163fcb13d416aa4e1a2c7d82115b3fd3d831241fd63|Shirts|
|21d56b6a011f91f4163fcb13d416aa4e1a2c7d82115b3fd3d831241fd63|Pants|
|166ca9b3a59edaf774d107533fba2c70ed309516376ce2693e92c777dd971c4b|Cardigans|

|email_hash|category|
|----------|--------|
|176146e4ae48e70df2e628b45dccfd53405c73f951c003fb8c9c09b3207e7aab|Wallets|
|63d42170fa2d706101ab713de2313ad3f9a05aa0b1c875a56545cfd69f7101fe|Purses|

Your script would output

|email_hash|category|filename|
|----------|--------|--------|
|21d56b6a011f91f4163fcb13d416aa4e1a2c7d82115b3fd3d831241fd63|Shirts|clothing.csv|
|21d56b6a011f91f4163fcb13d416aa4e1a2c7d82115b3fd3d831241fd63|Pants|clothing.csv|
|166ca9b3a59edaf774d107533fba2c70ed309516376ce2693e92c777dd971c4b|Cardigans|clothing.csv|
|176146e4ae48e70df2e628b45dccfd53405c73f951c003fb8c9c09b3207e7aab|Wallets|accessories.csv|
|63d42170fa2d706101ab713de2313ad3f9a05aa0b1c875a56545cfd69f7101fe|Purses|accessories.csv|

