import unittest
import pandas as pd
from src.data_loader import load_data

class TestDataLoader(unittest.TestCase):

    def setUp(self):
        self.test_csv_path = 'data/devtest.csv'
        self.expected_columns = ['label', 'query', 'query_rewriting']

    def test_load_data(self):
        df = load_data(self.test_csv_path)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(list(df.columns), self.expected_columns)
        self.assertFalse(df.empty)

    def test_data_integrity(self):
        df = load_data(self.test_csv_path)
        self.assertTrue(all(col in df.columns for col in self.expected_columns))

if __name__ == '__main__':
    unittest.main()