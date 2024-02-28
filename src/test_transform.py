import unittest
import pandas as pd 
from transform import Transform
class TestTransform(unittest.TestCase):
    def test_datetime(self):
        """
        HAPPY CASE 

        """
        df=pd.read_csv("../data/pizza_transaction_2015.csv")
        transformer = Transform(df,"order_date")
        df_transform=transformer.sort_date()
        expected_date = pd.Timestamp('2015-01-01 00:00:00')
        self.assertEqual(df_transform['order_date'].iloc[0], expected_date,"The date has not been changed into datetime type")

if __name__=="__main__":
    unittest.main()