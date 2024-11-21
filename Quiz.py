import sys
import os

"""A program to run a multiple choice quiz"""
    
# get user name with welcome message
# set score to zero
user = (input( "Hello and welcome to the Bootcamp Quiz Challenge," " Please enter your first name: "))
print(f"Good luck {user}" )
score = 0   

# set list of 10 multiple choice questions
# each question has 5 possible answers
# user prompted for answer, if answer is correct score is ammended
print("Q1 - Which of the following is a data type in Python? "
"A1 = letter,  "
"B1 = bigchar, "
"C1 = net, "
"D1 = string, "
"E1 = var ")

answer1 = (input (" Enter the correct answer (eg like F1)  "))
print(answer1)
if answer1 ==("D1" ):
    score = score + 1
else:
    score = score
print(score)

print("Q2 - Which keyword begins a function?  "
"A2 = funk,  "
"B2 = def, "
"C2 = func, "
"D2= define, "
"E2 = impf ")

answer2 = (input (" Enter the correct answer (eg like F1)  "))
print( answer2)
if answer2 ==("B2"):
    score = score + 1
else:
    score = score
print(score)

print("Q3 - A List is contained by   "
"A3 = @ @, "
"B3 = <>, "
"C3= {}, "
"D3= (), "
"E3 = [] ")

answer3 = (input (" Enter the correct answer (eg like F1)  "))
print( answer3)
if answer3 ==("E3"):
    score = score + 1
else:
    score = score
print(score)

print("Q4 - A dictionary uses  "
"A4 = words,  "
"B4 = keys, "
"C4= tuples, "
"D4= key pairs, "
"E4 = linked keys ")

answer4 = (input (" Enter the correct answer (eg like F1)  "))
print( answer4)
if answer4 ==("D4"):
    score = score + 1
else:
    score = score
print(score)

print("Q5 - What will print(-name_) print ?  "
"A5 = NameError: name 'name_' is not defined,  "
"B5 = SyntaxError: unexpected EOF while parsing, "
"C5 = nothing, "
"D5= what?, "
"E5 = system error! ")

answer5 = (input (" Enter the correct answer (eg like F1)  "))
print( answer5)
if answer5 ==("A5"):
    score = score + 1
else:
    score = score
print(score)

print("Q6 -Which statement is true  "
"A6 = Python is a low level language,  "
"B6 = Python only runs on windows OS, "
"C6= Python is interpreted, "
"D6 = Python is compiled, "
"E6 = Python is not used in industry")

answer6 = (input (" Enter the correct answer (eg like F1)  "))
print( answer6)
if answer6 ==("C6"):
    score = score + 1
else:
    score = score
print(score)

print("Q7 -  Which is correct? "
"A7 = ?/ = divide,  "
"B7 = d& = modulo, "
"C7 = x = multiply, "
"D7= ** = power, "
"E7 = !- = minus ")

answer7 = (input (" Enter the correct answer (eg like F1)  "))
print( answer7)
if answer7 ==("D7"):
    score = score + 1
else:
    score = score
print(score)

print("Q8 - DJANGO is a ?  "
"A8 = Banjo player,  "
"B8 = a web framework, "
"C8 = a better version of windows, "
"D8 = a python based game console, "
"E8 = all of the above ")

answer8 = (input (" Enter the correct answer (eg like F1)  "))
print( answer8)
if answer8 ==("B8"):
    score = score + 1
else:
    score = score
print(score)

print("Q9 - range() is used to ?  "
"A9 = fire bullets,  "
"B9 = drill into code, "
"C9 = specify a spread of items, "
"D9 = define a list, "
"E9 = delete values ")

answer9 = (input (" Enter the correct answer (eg like F1)  "))
print( answer9)
if answer9 ==("C9"):
    score = score + 1
else:
    score = score
print(score)

print("Q10 - bootcamps are ?  "
"A10 = for army deserters,  "
"B10 = for storing shoes, "
"C10 = tests for doctors, "
"D10= learning environments, "
"E10 = outdoor activity centres ")

# after final question is attempted score saved in score variable
# score is used to generate message to user using case 
answer10 = (input (" Enter the correct answer (eg like F1)  "))
print( answer10)
if answer10 ==("D10"):
    score = score + 1

    
# Users total printed
print((f"Your fnal score is, {score}" ))

# Message to user based on their total score
match score:
    case num if num <4:
        print("Oh dear - you need to practice more!")
    case num if num <7:
        print("Keep going!")
    case num if num <9:
        print("Great score!!")
    case num if num == 10:
        print("Brilliant! A Perfect  Score")

print("Thank you - you have completed the quiz")

"""def end():
    response = input("Press Q to Quit / C to try again")
    if response == "Q" | "q":
        exit()
    else:
        restartApp()
    
def restartApp():
    python = sys.executable
    os.execl(python, python, *sys.argv)"""
