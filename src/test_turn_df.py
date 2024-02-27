import pandas as pd 
import unittest
from turn_df import Extract
class TestExtract(unittest.TestCase):
    def test_turn_df(self):
        """
        HAPPY CASE:

        param:file_path:str - file path to the CSV file 
        return:pd.DataFrame - returns a dataframe from the csv file 
        This function is a test to see if the function does return a dataframe 
        """
        file_path = "../data/pizza_transaction_2015.csv"
        extractor =Extract(file_path)
        df = extractor.turn_df()
        self.assertIsInstance(df,pd.DataFrame,"DataFrame was not created")

if __name__=="__main__":
    unittest.main()