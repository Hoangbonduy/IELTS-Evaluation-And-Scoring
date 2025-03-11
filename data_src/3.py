import pandas as pd
import re

data = pd.read_csv('D:/Study/Deep learning/IELTS Writting Essays Scoring/data2/test_slow_module_dataset_2.csv')

# Xóa Overall Band Score trong data['evaluation']
def remove_overall_band_score(text):
    # Xóa từ Overall Band Score đến trước Feedback and Additional Comments: nếu có
    # Nếu không có Feedback and Additional Comments: thì xóa đến hết
    cleaned_text = re.sub(r"Overall Band Score(?:.|\n)*?(Feedback and Additional Comments|$)", r"\1", text)
    return cleaned_text

def replace_lexical_resource(text):
    # Sử dụng regex để thay thế Lexical Resource (Vocabulary) thành Lexical Resource
    return re.sub(r"Lexical Resource\s*\(?Vocabulary\)?", "Lexical Resource", text)

def format_essay(text):
    # Loại bỏ khoảng trắng thừa và nối các dòng lại thành đoạn văn liền mạch
    return "".join(line.strip() for line in text.splitlines())

for i in range(0,len(data)):
    data['essay'][i] = format_essay(data['essay'][i])
    data['evaluation'][i] = remove_overall_band_score(data['evaluation'][i])
    data['evaluation'][i] = replace_lexical_resource(data['evaluation'][i])
    
data.to_csv('D:/Study/Deep learning/IELTS Writting Essays Scoring/data2/test_slow_module_dataset_3.csv', index = False)