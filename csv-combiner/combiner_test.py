import unittest
import sys
from io import StringIO
import csv_combiner as csvc


class TestCombiner(unittest.TestCase):

    def test_no_file_given(self):
        """
        Tests behavior of combiner when no csv files are given.
        Error message should be outputted.
        """
        res = StringIO()
        sys.stdout = res
        csvc.combine(['./csv_combiner.py'])
        self.assertEqual(
            res.getvalue(), 'Error: Must provide at least one csv file to combine\n')

    def test_unknown_file(self):
        """
        Tests behavior of combiner when provided file cannot be found.
        Error message should be outputted
        """
        res = StringIO()
        sys.stdout = res
        csvc.combine(['./csv_combiner.py', './unknown_file.csv'])
        self.assertEqual(
            res.getvalue(), 'Error: File "./unknown_file.csv" could not be found\n')

    def test_noncsv_file(self):
        """
        Tests behavior of combiner when valid file is given, but not csv.
        Error message should be outputted.
        """
        res = StringIO()
        sys.stdout = res
        csvc.combine(['./csv_combiner.py', './test_csv/noncsv.txt'])
        self.assertEqual(res.getvalue(
        ), 'Error: Invalid file type: "./test_csv/noncsv.txt". File must be .csv\n')

    def test_empty_file(self):
        """
        Tests behavior of combiner when empty file is given.
        This is an edge case and should produce file with empty filename column.
        """
        res = StringIO()
        sys.stdout = res
        csvc.combine(['./csv_combiner.py', './test_csv/empty.csv'])
        self.assertEqual(res.getvalue(), 'filename\n\n')

    def test_multiple_files(self):
        """
        Tests behavior of combiner when more than 2 files are provided as command line arguments.
        Rows from each file should be combined into one large csv, the same as if there were only 
        2 files.
        """
        res = StringIO()
        sys.stdout = res
        csvc.combine(['./csv_combiner.py', './test_csv/test2.csv',
                     './test_csv/test3.csv', './test_csv/test4.csv'])

        true_file = open('./test_csv/multiple_test.csv')
        true = true_file.read()
        true_file.close()

        self.assertEqual(res.getvalue(), true)

    def test_diff_num_columns(self):
        """
        Tests behavior of combiner when csv files contain different number of columns.
        Columns from each file should be included in each row with empty value for non-applicable columns.
        "filename" column should always be the last column.
        """
        res = StringIO()
        sys.stdout = res
        csvc.combine(
            ['./csv_combiner.py', './test_csv/test1.csv', './test_csv/test2.csv'])

        true_file = open('./test_csv/diff_col_test.csv')
        true = true_file.read()
        true_file.close()

        self.assertEqual(res.getvalue(), true)


if __name__ == '__main__':
    unittest.main()
