import pandas as pd

data = pd.read_csv('D:/Study/Deep learning/IELTS Writting Essays Scoring/data2/slow_module_dataset_2.csv')
data2 = pd.read_csv('D:/Study/Deep learning/IELTS Writting Essays Scoring/data2/slow_module_dataset_4.csv')

# Kiểm tra xem có tồn tại Feedback and Additional Comments trong text không
def check_feedback(text):
    return "Feedback and Additional Comments" in text

k = []

for i in range(0,len(data)):
    if check_feedback(data['evaluation'][i]) == False:
        k.append(i)

# Xóa đi những phần tử không có Feedback and Additional Comments
data2 = data2.drop(k)

print(k[:10])

# Lưu
data2.to_csv('D:/Study/Deep learning/IELTS Writting Essays Scoring/data2/slow_module_dataset_5.csv', index = False)