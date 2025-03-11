import re
import pandas as pd

def process(text):
    k = re.sub(r'\**-? *Suggested (Band|Overall Band) Score(?: \([^)]*\))?:\**', '', text).strip()
    k = re.sub(r'\[\d+\.\d+\]|\[\d+\]|\b\d+\.\d+\b|\b\d+\b', '', k).strip()
    return k

# Đọc dữ liệu
data = pd.read_csv('D:/Study/Deep learning/IELTS Writting Essays Scoring/data/task2/test.csv')
for i in range(0,len(data)):
    data['evaluation'][i] = process(data['evaluation'][i])
    #print(i)
    
# Xóa cột band
data = data.drop('band', axis=1)
    
# Lưu dữ liệu
data.to_csv('D:/Study/Deep learning/IELTS Writting Essays Scoring/data2/test_slow_module_dataset.csv', index = False)