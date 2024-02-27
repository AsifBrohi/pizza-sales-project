import pandas as pd 

class Extract:
    def __init__(self,file_path:str) -> None:
        self.file_path = file_path
    def turn_df(self:str)->pd.DataFrame:
        """
        This function uses a file path and using pandas creates 
        a dataframe. 
        :param:file_path:str - Releative path to the CSV file
        :return:pd.Dataframe - Returns a dataframe 

        """
        try:

            df = pd.read_csv(self.file_path)
            return df
        except FileNotFoundError as error:
            return error
         
if __name__=="__main__":
    file_path = "./data/pizza_transaction_2015.csv"
    extractor=Extract(file_path)
    df=extractor.turn_df()
    print(df)
    