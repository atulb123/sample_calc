import pandas as pd
from sqlalchemy import create_engine


class Calculation:

    def perform_add(self, num1, num2):
        return num1 + num2

    def perform_sub(self, num1, num2):
        return num1 - num2

    def perform_nul(self, num1, num2):
        return num1 + num2

    def perform_div(self, num1, num2):
        return num1 / num2

    def copy_df_to_db(self, file_path, table_name):
        conn_string = f'postgresql://postgres:wh0_kn0wz_wh4t_3v1l_1urks_th3_sh4d0w_kn0z@localhost:5400/pipeline'
        db = create_engine(conn_string)
        conn = db.connect()
        df = pd.read_csv(file_path)
        df.to_sql(table_name, con=conn, if_exists='replace', index=False)
        conn.close()

    def buggy_function(self):
        x = 10
        y = 0
        result = x / y
        print("This line will never be executed.")
        return result

