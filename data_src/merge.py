import pandas as pd

df1 = pd.read_csv('D:/Study/Deep learning/IELTS Writting Essays Scoring/data2/0_3133.csv')
df2 = pd.read_csv('D:/Study/Deep learning/IELTS Writting Essays Scoring/data2/3134_4499.csv')
df3 = pd.read_csv('D:/Study/Deep learning/IELTS Writting Essays Scoring/data2/4500_5499.csv')
df4 = pd.read_csv('D:/Study/Deep learning/IELTS Writting Essays Scoring/data2/5500_9832.csv')

df = pd.concat([df1, df2, df3, df4], ignore_index=True)
df.to_csv('D:/Study/Deep learning/IELTS Writting Essays Scoring/data2/0_9832.csv', index=False)