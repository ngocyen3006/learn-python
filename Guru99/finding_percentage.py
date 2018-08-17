# 2 <= n <= 10
# 0 <= Marks <= 100
# ex:
# n = 2
# harsh 25 26.5 28
# anurag 26 28 30
# Harsh
# kq = 26.50


n = int(input())
student_marks = {}

for i in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    average = sum(scores) / len(scores)
    student_marks[name] = average

query_name = input()
print("%.2f" % student_marks[query_name])
