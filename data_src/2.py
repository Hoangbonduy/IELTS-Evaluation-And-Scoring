import pandas as pd
import re

data = pd.read_csv('D:/Study/Deep learning/IELTS Writting Essays Scoring/data2/test_slow_module_dataset.csv')

def clean_and_adjust(text):
    # Xóa các ký tự *, #, - , < và >
    cleaned_text = re.sub(r'[*#-<>:]', '', text)
    
    # Xóa đi Strengths: , Areas for Improvement: , Suggestions for Enhancement: , Strategies for enhancement:
    cleaned_text = re.sub(r'\s*(?:Strengths|strengths|Areas for Improvement|Areas for improvement|areas for improvement|Suggestions for Enhancement|Strategies for enhancement|suggestions for Enhancement|suggestions for enhancement|strategies for Enhancement|strategies for enhancement)', '', cleaned_text)
    
    return cleaned_text

def remove_leading_spaces(text):
    """
    Loại bỏ khoảng trắng ở đầu mỗi dòng trong chuỗi đầu vào.
    """
    # Tách chuỗi thành từng dòng
    lines = text.splitlines()
    
    # Loại bỏ khoảng trắng đầu dòng cho từng dòng
    cleaned_lines = [line.lstrip() for line in lines]
    
    # Ghép lại các dòng thành chuỗi hoàn chỉnh
    cleaned_text = "\n".join(cleaned_lines)
    return cleaned_text

def remove_blank_lines(text):
    # Tách văn bản thành từng dòng, loại bỏ dòng trắng và gộp lại thành đoạn văn bản
    lines = text.splitlines()
    cleaned_lines = [line for line in lines if line.strip()]  # Loại bỏ dòng chỉ chứa khoảng trắng
    return "\n".join(cleaned_lines)

for i in range(0,len(data)):
    data['evaluation'][i] = clean_and_adjust(data['evaluation'][i])
    
    data['evaluation'][i] = remove_leading_spaces(data['evaluation'][i])
    
    data['evaluation'][i] = remove_blank_lines(data['evaluation'][i])
    
# data = data.drop('band', axis=1)

data.to_csv('D:/Study/Deep learning/IELTS Writting Essays Scoring/data2/test_slow_module_dataset_2.csv', index = False)