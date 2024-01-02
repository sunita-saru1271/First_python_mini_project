print("Welcome to the Python MCQ (Multiple Choice Questions)")

Name=input("Please enter you name: ").upper()
print("***Welcome", Name,"***" "\n")

playing = input("Do you want to play (Y/N) \n").upper()

if playing != 'Y':
    quit()

print("Lets begin the quiz!!!\nYou need to score 80% to pass\n")

score=0

ans=input("Who developed the Python language? \n" +
          "a) Zim Den\n" +
          "b) Guido van Rossum\n"+
          "c) Niene Stom\n"+
          "d) Wick van Rossum\n")
if ans.lower()=="b":
    print("Correct")
    print("Explanation: Python language was developed by Guido van Rossum in the Netherlands.\n")
    score +=1

else:
    print("Incorrect\n")


ans=input("What is the maximum possible length of an identifier? \n" +
          "a) 16\n" +
          "b) 32\n"+
          "c) 64\n"+
          "d) None of these above\n")
if ans.lower()=="d":
    print("Correct")
    print("Explanation: The maximum possible length of an identifier is not defined in the python language. It can be of any number.\n")
    score +=1

else:
    print("Incorrect\n")

ans=input("In which year was the Python language developed? \n" +
          "a) 1995\n" +
          "b) 1972\n"+
          "c) 1981\n"+
          "d) 1989\n")
if ans.lower()=="d":
    print("Correct")
    print("Explanation: Python language was developed by Guido van Rossum in 1989.\n")
    score +=1

else:
    print("Incorrect\n")

ans=input("In which language is Python written? \n" +
          "a) English\n" +
          "b) PHP\n"+
          "c) C\n"+
          "d) All of the above\n")
if ans.lower()=="c":
    print("Correct")
    print("Explanation: Python is written in C programming language, and it is also called CPython.\n")
    score +=1

else:
    print("Incorrect\n")

ans=input("Which one of the following is the correct extension of the Python file? \n" +
          "a) .py\n" +
          "b) .python\n"+
          "c) .p\n"+
          "d) None of the above\n")
if ans.lower()=="a":
    print("Correct")
    print("Explanation: .py is the correct extension of the Python file. \n")
    score +=1

else:
    print("Incorrect\n")

ans=input("In which year was the Python 3.0 version developed? \n" +
          "a) 2008\n" +
          "b) 2000\n"+
          "c) 2010\n"+
          "d) 2005\n")
if ans.lower()=="a":
    print("Correct")
    print("Explanation: Python 3.0 version was developed on December 3, 2008. \n")
    score +=1

else:
    print("Incorrect\n")

ans=input(" What do we use to define a block of code in Python language? \n" +
          "a) Key\n" +
          "b) Brackets\n"+
          "c) Indentation\n"+
          "d) None of these\n")
if ans.lower()=="c":
    print("Correct")
    print("Explanation: Python uses indentation to define blocks of code. Indentations are simply spaces or tabs used as an indicator that is part of the indent code child.\n As used in curly braces C, C++, and Java. \n")
    score +=1
else:
    print("Incorrect\n")

ans=input("Which character is used in Python to make a single line comment? \n" +
          "a) / \n" +
          "b) // \n"+
          "c) #\n"+
          "d) !\n")
if ans.lower()=="c":
    print("Correct")
    print("Explanation: # character is used in Python to make a single-line comment.\n")
    score +=1

else:
    print("Incorrect\n")

ans=input("Which of the following statements is correct regarding the object-oriented programming concept in Python? \n" +
          "a) Classes are real-world entities while objects are not real \n" +
          "b) Objects are real-world entities while classes are not real \n"+
          "c) Both objects and classes are real-world entities \n"+
          "d) All of the above \n")
if ans.lower()=="b":
    print("Correct")
    print("Explanation: None \n")
    score +=1

else:
    print("Incorrect\n")

ans=input("What is the method inside the class in python language? \n" +
          "a) Object \n" +
          "b) Function \n"+
          "c) Attribute \n"+
          "d) Argument \n")
if ans.lower()=="b":
    print("Correct")
    print("Explanation: Function is also known as the method. \n")
    score +=1

else:
    print("Incorrect\n")

print("You have answered " + str(score) + " questions correct")

per=int((score/10)*100)

if per >= 80:
    print("You have scored " + str(per) + " %.")
    print("Congratulations!! you have passed the exam.")
    
else:
    print("Scored " + str(per) + " %.")
    print("Failed!! Please Try again")
    

