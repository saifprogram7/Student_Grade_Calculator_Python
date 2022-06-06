print("Welcome to the Grade Calculator")
print("Lets find out the grade you have!\n")
def gradecalculator(module_1_marks,module_2_marks,module_3_marks,module_4_marks,module_5_marks):
    result = module_1_marks+module_2_marks+module_3_marks+module_4_marks+module_5_marks
    result = result / 5
    if (result >=80):
        print("Your grade is an A!")
    if (result >=70 and result <=80):
        print("Your grade is a B!")
    if (result >=60 and result <=70):
        print("Your grade is a C!")
    if (result <=60):
        print("You have Failed this year!")
    return result
while True:    
    user = input("Please enter your name: ")
    if user == "end":
        break
    else:    
        module_1_marks = int(input("Please enter your Module 1 marks out of 100: "))
        module_2_marks = int(input("Please enter your Module 2 marks out of 100: "))
        module_3_marks = int(input("Please enter your Module 3 marks out of 100: "))
        module_4_marks = int(input("Please enter your Module 4 marks out of 100: "))
        module_5_marks = int(input("Please enter your Module 5 marks out of 100: "))
        gradecalculator(module_1_marks,module_2_marks,module_3_marks,module_4_marks,module_5_marks)