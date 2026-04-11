# 12）给定一个字典student_scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 88}，
# 编写一个程序，将每个学生的分数增加 5 分，并将结果存储在一个新的字典updated_scores中。
student_scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 88}
updated_scores=dict()
keys=student_scores.keys()
for k in keys:
    updated_scores[k]=student_scores[k]+5
print(updated_scores)