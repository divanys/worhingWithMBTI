import json
from scriptFirst import questions, answer_a, answer_b

result = []
for i in range(len(questions)):
    result.append({
        "question": questions[i],
        "answer": [answer_a[i], answer_b[i]]
    })

with open("worhingWithMBTI/QandA/questions.json", "w") as f:
    json.dump(result, f, ensure_ascii=False)
