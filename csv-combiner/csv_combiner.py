import pandas as pd
import sys
import os


def create_df(filename):
    """
    Creates new DataFrame object from csv file provided by filename parameter.
    Adds 'filename' column and returns DataFrame object
    """
    df = pd.DataFrame()
    # if file is empty, simply add 'filename' column and return
    if (os.path.getsize(filename) > 0):
        df = pd.read_csv(filename, index_col=False)
    df['filename'] = os.path.basename(filename)
    return df


def valid_args(args):
    """
    Validates command line arguments. Returns false if any file name can't be found, 
    file not csv, or no filenames provided. Returns true otherwise
    """
    if len(args) < 2:
        print("Error: Must provide at least one csv file to combine")
        return False

    for a in args[1:]:
        if not os.path.isfile(a):
            print(f'Error: File "{a}" could not be found')
            return False

        if not os.path.splitext(a)[-1] == '.csv':
            print(f'Error: Invalid file type: "{a}". File must be .csv')
            return False

    return True


def combine(args):
    """
    Combines csv files specified within command line arguments into one csv file
    and outputs combined file to stdout
    """
    if valid_args(args):
        combined = pd.concat([create_df(f) for f in args[1:]], axis=0)
        col = list(combined.columns)
        col.remove("filename")
        print(combined.loc[:, col + list(["filename"])
                           ].to_csv(index=False, lineterminator='\n'))


def main():
    combine(sys.argv)


if __name__ == "__main__":
    main()
