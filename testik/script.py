import re


with open('worhingWithMBTI/testik/data.txt', 'r') as f:
    text = f.read()


questions = re.findall(r"\d+\.\s(.+?)\n", text)
answers = re.findall(r"\n\s*(\w\))\s*(.+?)(?=\n\s*\w|\Z)", text, flags=re.DOTALL)

a_answers = []
b_answers = []

for answer in answers:
    if answer[0].startswith("а"):
        a_answers.append(answer[1])
    elif answer[0].startswith("б"):
        b_answers.append(answer[1])

a1 = []
b1 = []

for i in range(len(a_answers)):
    a1.append(a_answers[i].replace(';', '').replace('.', '').rstrip())
    b1.append(b_answers[i].replace('.', '').rstrip())
  
print(a1)
print(b1)
