import pandas as pd
from sqlalchemy import create_engine
df = pd.read_csv('final_seq.csv')
engine = create_engine('postgresql://ubuntu:hello@0.0.0.0:5432/chad_db')

while True:
    if len(df) >= 100:
        first_ten = df[:100]
        df = df[100:]
    else:
        first_ten = df
        break
    first_ten.to_sql("seq", engine, if_exists='append')
    print(len(df), len(first_ten))

    

