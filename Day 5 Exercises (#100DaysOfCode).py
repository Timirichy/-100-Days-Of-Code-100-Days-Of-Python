                #LOOPS

                # 050
                # Average Height

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
                # This is the short solution, but for concept understanding, we do not use len or sum
# total_height = sum(student_heights)
# number_of_student = len(student_heights)
# average_height = round(total_height / number_of_student)
# print(average_height)

                # Long Method
            # Adding(Sum function)
total_height = 0
for height in student_heights:
    total_height = total_height + height
print(total_height)
            #Counting (Len function)
number_of_student = 0
for height in student_heights:
    number_of_student += 1
print(number_of_student)

average_height = round(total_height / number_of_student)
print(average_height)