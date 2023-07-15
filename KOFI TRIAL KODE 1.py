
# #print("Hello world")
# exam_score = int(input("What is your mark:"))
# if exam_score >= 90:
#     print("GPA 4.0")
# elif exam_score >= 80:
#     print("GPA 3.75")
# elif exam_score >= 70:
#     print("GPA 3.0")
# elif exam_score >= 60:
#     print("GPA 2.0")
# elif exam_score >= 50:
#         print("CONGRATS you passed")
# else:
#     print("loser")



def score_calculator(exam_score):
    if exam_score >= 90:
        return "GPA 4.0"
    elif exam_score >= 80:
        return "GPA 3.75"
    elif exam_score >= 70:
        return "GPA 3.0"
    elif exam_score >= 60:
        return "GPA 2.0"
    elif exam_score >= 50:
        return "CONGRATS you passed"
    else:
        return "loser"

instance1 = score_calculator(90)
print(instance1)