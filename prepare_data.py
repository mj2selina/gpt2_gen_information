import pandas as pd
import os
from utils.cleaner import cleaning
path = 'origin_data'
output_path = 'data'

df = pd.DataFrame()

for file in os.listdir(path):
    xls = pd.read_excel(os.path.join(path,file))
    df = pd.concat([df,xls],axis=0)
    # print(df.head(0))

df = df.dropna(subset='Content')

def clean(df):
    text_data = []
    for item in list(df['Content']):
        text_data.append(cleaning(item))
    return text_data

text_data = clean(df)
with open(os.path.join(output_path,'comment.txt'),'w') as f:
    f.write('\n'.join(text_data))
