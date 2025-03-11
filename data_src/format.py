import re

def extract_relevant_lines(feedback):
    # Define the pattern to match the relevant lines
    pattern = r".*(Lexical Resource|Lexical Resource \(Vocabulary\)|Grammatical Range and Accuracy|Coherence and Cohesion|Overall Band Score).*"
    # Find all matches in the feedback string
    matches = re.findall(pattern, feedback)
    return matches

def extract_band_scores(feedback):
    # Define the pattern to match the band scores
    pattern = r"\*\*(.*?)\*\*: (\d\.\d)"
    # Find all matches in the feedback string
    matches = re.findall(pattern, feedback)
    # Convert matches to a dictionary
    scores = {match[0]: float(match[1]) for match in matches}
    return scores

feedback = """
## Task Achievement:
- The candidate has adequately addressed the task by presenting arguments for and against the reliability of interviews as a method of employee selection.
- The essay covers all aspects of the task, providing relevant examples and supporting arguments.
- However, the essay could have benefited from a more concise and structured approach, as some ideas are presented in a slightly disorganised manner.
**Suggested Band Score: 6.0**

## Coherence and Cohesion:
- The essay lacks a clear and logical structure, with transitions between sentences and paragraphs appearing somewhat abrupt.
- The use of connecting words and phrases is limited, affecting the overall flow and coherence of the text.
- The essay would benefit from a more organised approach, with clear topic sentences and supporting evidence presented in a cohesive manner.
**Suggested Band Score: 5.5**

## Lexical Resource (Vocabulary):
- The candidate has used a limited range of vocabulary, with some inaccuracies and overuse of certain words.
- For example, the word "manager" is used repeatedly without variation.
- The essay would benefit from a more diverse and appropriate use of vocabulary, as well as the correction of grammatical errors.
**Suggested Band Score: 5.0**

## Grammatical Range and Accuracy:
- The essay exhibits a limited range of sentence structures and grammatical accuracy.
- There are several grammatical errors, including incorrect verb forms and sentence construction.
- For example, "However, according to, my perspective interviews are not enough" contains a grammatical error.
- The essay would benefit from a more varied use of sentence structures and improved grammatical accuracy.
**Suggested Band Score: 5.0**

## Overall Band Score:
- The essay demonstrates a partial fulfillment of the task requirements, with some relevant arguments presented but a lack of organisation and coherence.
- The use of vocabulary is limited and inaccurate, and the grammatical accuracy is below the required standard.
**Suggested Overall Band Score: 5.5**

## Feedback and Additional Comments:
- The essay would benefit from a more structured approach, with clear topic sentences and supporting evidence presented in a logical order.
- The candidate should focus on expanding their vocabulary and improving their grammatical accuracy to enhance the overall quality of their writing.
- Additionally, the use of specific examples and real-life scenarios would strengthen the arguments presented in the essay.

Extract the band scores like:
Citeration: Score.
**Lexical Resource:** 5.0
**Grammatical Range and Accuracy:** 5.0
**Coherence and Cohesion:** 5.5
**Overall Band Score:** 5.5
"""

# Extract relevant lines
relevant_lines = extract_relevant_lines(feedback)
# Extract band scores
band_scores = extract_band_scores(feedback)

# Print relevant lines with corresponding band scores
for line in relevant_lines:
    criterion = line.split(":")[0].strip()
    if criterion in band_scores:
        print(f"{line}: {band_scores[criterion]}")