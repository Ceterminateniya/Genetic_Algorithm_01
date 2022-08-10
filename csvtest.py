import pandas as pd
import os


path = '.\\data.xlsx'
data = pd.read_excel(path)

file=os.getcwd()+'/'+'SGA_result.csv'
data01=pd.DataFrame(data)
data01.to_csv(file,index=False)