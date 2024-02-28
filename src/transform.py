import pandas as pd 

class Transform:
    
    def __init__(self,df:pd.DataFrame,column_name:str) -> None:

        """
        :param:df:pd.DataFrame-The dataframe that you want to change
        :param:column_name:str-The column you want to use to create dimension table
        :return:pd.DataFrame:-Returns dataframe which you edited 

        """
        self.df=df
        self.column_name=column_name
    
    def sort_date(self)->pd.DataFrame:
        """
        This function changes the order_date column into datetime type

        """
        self.df["order_date"]=self.df["order_date"].astype('datetime64[ns]')
        return self.df
    
    def dimenstion_data(self)->pd.DataFrame:
        """
        This function drops duplicate values within a certain column
        Then resets the index, and returns new df

        """
        df_new = self.df[self.column_name].drop_duplicates()
        df_new.reset_index(drop=True,inplace=True)
    
        return df_new

if __name__=="__main__":
    df = pd.read_csv("../data/pizza_transaction_2015.csv")
    transformer = Transform(df,"pizza_name")
    df_transformer = transformer.sort_date()
    df_name_dim=transformer.dimenstion_data()
    print(df_name_dim)
    