import pandas as pd
import re

# --- Bước 1: Đọc file điểm ---
# File cleaned.csv có các cột: "Task Achievement", "Coherence and Cohesion", "Lexical Resource", "Grammatical Range and Accuracy"
scores_df = pd.read_csv("D:/Study/Deep learning/IELTS Writting Essays Scoring/data2/cleaned_0_9830.csv", encoding="utf-8")
# Chuyển một dòng điểm thành dictionary; giả sử rằng mỗi dòng của scores_df tương ứng với một mẫu (cùng thứ tự với file evaluations)
# Nếu file chứa 1 dòng duy nhất với điểm cho 4 tiêu chí, hãy chuyển nó thành một dictionary
# Ví dụ, nếu file cleaned.csv chỉ có 1 dòng, bạn có thể làm:
if len(scores_df) == 1:
    scores_global = scores_df.iloc[0].to_dict()
else:
    scores_global = None  # sẽ xử lý theo từng dòng

# --- Bước 2: Đọc file CSV chứa prompt, essay, evaluation ---
eval_df = pd.read_csv("D:/Study/Deep learning/IELTS Writting Essays Scoring/data2/slow_module_dataset_4.csv", encoding="utf-8")

def update_evaluation_text(evaluation_text, scores_row):
    """
    Hàm nhận vào một evaluation text và một dictionary scores_row (criterion: score)
    và chuyển đổi theo yêu cầu:
      - Mỗi block bắt đầu bằng dòng "-" (tiêu chí).
      - Thu thập tất cả các dòng bắt đầu bằng "+" (nhận xét) cho block đó.
      - Sau đó, xuất header "* Expert Explanation:".
      - Xử lý các dòng nhận xét: chèn xuống dòng trước từ mới bắt đầu bằng chữ in hoa (nếu phía trước là chữ thường),
        sau đó tách thành các câu và thêm dấu "+ " ở đầu mỗi câu.
      - Cuối block, nếu tiêu chí không phải "Feedback and Additional Comments" và có trong scores_row, 
        chèn "* Expert Score (criterion): <score>".
    """
    # Tách theo dòng
    lines = evaluation_text.splitlines()
    output_lines = []
    current_criterion = None
    explanation_block = []  # lưu các dòng nhận xét cho block hiện tại

    for line in lines:
        stripped = line.strip()
        if stripped.startswith('-'):
            # Nếu có block trước, xử lý và in ra
            if current_criterion is not None and explanation_block:
                output_lines.append("* Expert Explanation:")
                for exp in explanation_block:
                    # Chèn xuống dòng trước từ mới bắt đầu bằng chữ in hoa (sau chữ thường)
                    formatted = re.sub(r'(?<=[a-z])\s+(?=[A-Z])', '\n', exp)
                    # Tách theo newline và thêm dấu "+"
                    for sentence in formatted.split('\n'):
                        if sentence.strip():
                            output_lines.append("+ " + sentence.strip())
                # Sau đó, nếu tiêu chí có điểm (và không phải Feedback and Additional Comments)
                if current_criterion != "Feedback and Additional Comments" and current_criterion in scores_row:
                    output_lines.append("* Expert Score ({}): {}".format(current_criterion, scores_row[current_criterion]))
            # Reset block cho tiêu chí mới
            # Trích xuất tên tiêu chí (loại bỏ dấu "-" và ":" ở cuối)
            current_criterion = stripped.lstrip('-').rstrip(':').strip()
            output_lines.append(line.rstrip('\n'))  # giữ nguyên dòng tiêu chí
            explanation_block = []
        elif stripped.startswith('+'):
            # Dòng nhận xét, thêm vào block (loại bỏ dấu "+")
            explanation_block.append(stripped.lstrip('+').strip())
        else:
            # Dòng khác (nếu có) giữ nguyên
            output_lines.append(line.rstrip('\n'))
    
    # Xử lý block cuối cùng (nếu có)
    if current_criterion is not None and explanation_block:
        output_lines.append("* Expert Explanation:")
        for exp in explanation_block:
            formatted = re.sub(r'(?<=[a-z])\s+(?=[A-Z])', '\n', exp)
            for sentence in formatted.split('\n'):
                if sentence.strip():
                    output_lines.append("+ " + sentence.strip())
        if current_criterion != "Feedback and Additional Comments" and current_criterion in scores_row:
            output_lines.append("* Expert Score ({}): {}".format(current_criterion, scores_row[current_criterion]))
    
    return "\n".join(output_lines)

# --- Bước 3: Áp dụng xử lý cho từng mẫu ---
updated_evaluations = []
# Nếu scores_global đã được thiết lập (1 dòng điểm cho toàn bộ), sử dụng nó cho mọi mẫu;
# Ngược lại, nếu scores_df có số dòng tương ứng, ta dùng từng dòng
for i, row in eval_df.iterrows():
    evaluation_text = row["evaluation"]
    if scores_global is not None:
        scores_row = scores_global
    else:
        # Giả sử scores_df có cùng số dòng với eval_df
        scores_row = scores_df.iloc[i].to_dict()
    updated_eval = update_evaluation_text(evaluation_text, scores_row)
    updated_evaluations.append(updated_eval)

# Thêm cột evaluation mới vào DataFrame
eval_df["evaluation"] = updated_evaluations

# --- Bước 4: Xuất ra file CSV mới với các cột prompt, essay, evaluation ---
eval_df[["prompt", "essay", "evaluation"]].to_csv("updated_evaluations.csv", index=False, encoding="utf-8")