#                              KAUN BANEGA CROREPATI!!!!

print("WELCOME TO THE KAUN BANEGA CROREPATI!")
print("Here is your 1st question")
question = "Are Tuple Mutable"
option = "A: 'yes' B:'no' "
print(question)
print(option)
prize = 0
answer = input("Enter your Answer")
if(answer == "B"):
    print("Correct answer")
    prize = prize + 10000
else:
    print("Wrong Answer :(")

print("Your prize is", prize)

question2 = "What is the capital of India"
option2 = "A: 'Delhi' B:'Mumbai' C:'Kolkata' D:'Chennai'"
print(question2)
print(option2)
answer2 = input("Enter your answer")
if(answer2 == "A"):
    print("Correct Answer")
    prize = prize + 10000
else:
    print("Sorry Wrong answer")

print("Your prize is", prize)

question3 = "What is the capital of USA"
option3 = "A: 'New York' B:'Texas' C:'California' 'D: 'Washington D.C'"
print(question3)
print(option3)
answer3 = input("Enter your answer")
if(answer3 == "D"):
    print("Correct Answer :)")
    prize = prize + 10000
else:
    print("Sorry Better luck next time!")

print("So Your current prize is:", prize)

Specialquestion = "Who is the founder of Python"
option4 = "A: 'Guido Van Rossum' B:'Bill Gates' C:'Mark Zuckerberg' D:'Steve Jobs'"
print(Specialquestion)
print(option4)
answer4 = input("Enter your answer")
if(answer4 == "A"):
    print("Correct Answer :)")
    prize = prize + 20000
else:
    print("Sorry! You have not won the game but you won some prizes!!")


if(prize == 50000):
    print("Congratulations! You have won the game")
    print("With the amount of", prize, "wohooooo!!!")
else:
    print("Sorry but you won the prizes of amount", prize)