import pandas as pd
import re

def format_text(lines):
    categories = [
        "Task Achievement", "Coherence and Cohesion",
        "Lexical Resource", "Grammatical Range and Accuracy",
        "Feedback and Additional Comments"
    ]
    formatted_lines = []
    
    if not isinstance(lines, str):
        lines = str(lines)  # Chuyển đổi thành chuỗi nếu cần
    
    for line in lines.split('\n'):
        if any(line.startswith(category) for category in categories):
            formatted_lines.append(f"- {line}:")
        else:
            formatted_lines.append(f"+ {line}")
    
    return '\n'.join(formatted_lines)

data = pd.read_csv('D:/Study/Deep learning/IELTS Writting Essays Scoring/data2/test_slow_module_dataset_3.csv')

for i in range(0,len(data)):
    data['evaluation'][i] = format_text(data['evaluation'][i])
    
data.to_csv('D:/Study/Deep learning/IELTS Writting Essays Scoring/data2/test_slow_module_dataset_4.csv', index = False)