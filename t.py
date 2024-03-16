import pandas as pd
data_url = 'loan_applic.csv'  # Replace this with your dataset URL or local path
df = pd.read_csv(data_url)
pd.set_option('display.max_rows', None)
print(df['Outcome'])
