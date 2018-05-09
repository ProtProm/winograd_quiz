
#this module implements pseudo-random number generators for various distributions
import random

#dictionary with the difficulties, question and answers intented and classified by type
data = {
    "easy": {
        "question" :  '''
        The city councilmen refused the demonstrators a permit because they feared violence. (__1__) feared violence.
        The city councilmen refused the demonstrators a permit because they advocated violence. (__2__) advocated violence.
        Sam and Amy are passionately in love, but Amy's parents are unhappy about it. It is because (__3__) are snobs.
        Sam and Amy are passionately in love, but Amy's parents are unhappy about it. It is because (__4__) are fifteen.
        ''',
        "answer" : ["the city councilmen","the demonstrators","amy's parents","sam and amy"],
    },
    "medium": {
        "question" : '''
        John was doing research in the library when he heard a man humming and whistling. (__1__) was annoyed.
        John was doing research in the library when he heard a man humming and whistling. (__2__) was annoying.
        Mary took out her flute and played one of her favorite pieces. Mary has loved (__3__) since she was a child.
        Mary took out her flute and played one of her favorite pieces. Mary has had (__4__) since she was a child.
        ''',
        "answer" : ["john","the hummer","the piece","the flute"],
    },
    "hard": {
        "question" :  '''
        The city councilmen refused the demonstrators a permit because they feared violence. (__1__) feared violence.
        The city councilmen refused the demonstrators a permit because they advocated violence. (__2__) advocated violence.
        Sam and Amy are passionately in love, but Amy's parents are unhappy about it. It is because (__3__) are snobs.
        Sam and Amy are passionately in love, but Amy's parents are unhappy about it. It is because (__4__) are fifteen.
        ''',
        "answer" : ["joan","jane","the chatbots","the judges"],
    }
}

#the blanks to fill in question section with user_input, it has to match the answer section
blanks_to_fill = ["__1__","__2__", "__3__", "__4__"]

#title
print ('''

>>> WINOGRAD SCHEMAS CHALLENGE <<<

''')

#user input the number of lives wich  will have in each challenge shorted by difficulty
lives = int(input("How many lives do you want? "))

#user chooses difficulty in order to start the challenge or press enter to end the module-challenge
#this function takes no inputs and returns the function level choosen after having choose difficulty
def level_choice():
    level = input("Choose difficulty: easy, medium, hard or nothing: ").lower()
    if level == "easy":
        return level_choosen(level)
    elif level == "medium":
        return level_choosen(level)
    elif level == "hard":
        return level_choosen(level)
    else:
        return "Well done anyways!"

#this function takes as input the level choosen, and as output:
#prints the appropiate question in the dictionary and asks the user to fill the blanks
#also returns the function challenge, with the question and answer correspondent to the level choosen, as well as the lives choosen
def level_choosen(level):
    print(data[level]['question'])
    print("Fill in the blanks.")
    return challenge(data[level]['question'], data[level]['answer'], lives)


#this function uses the question answer choosen in the difficulty, and the lives in in (input)lives
#index in 0 in order to keep track to know when are all the blanks filled correctly
#if the user input is the same as the answer numered the blank numered will be replaced by it and the index will increase in one in order to pass to the next blank to filled
#if the length of answer is the same as index means that there are no more blanks to fill, meaning the user has passed the test in the difficulty chossen
#if not, the question with the blanks correctly anwsered having been substituted will be ran, and the user will be asked to write the blank again
#if the lives are more than 1, if they're 1 the challenge ends printing "0 lives left"

#as inputs it has question, answer, and lives previously choosen
#as output it returns level_choice if the user has no lives left
def challenge(question, answer, lives):
    index = 0
    while index < len(answer):
        user_input = input("Write word to fill " + str(blanks_to_fill[index]) + " : ").lower()
        if user_input == answer[index]:
            question = question.replace(blanks_to_fill[index], answer[index])
            index += 1
            print(correct_guess(answer, question, index))
        else:
            if lives == 1:
                print("0 lives left!")
                return level_choice()
            else:
                lives -= 1
                print(question)

#function that runs in case of correct guess

#input: answer and question previously choosen, and index(kept in track)
#output: if the length is not equal, it returns the next question
        #if the length of the answer section is equal to the index having keeped it in track:
        #means that the challenge is passed so before it ends it prints the question with the correct words for the blanks
def correct_guess(answer, question, index):
    if len(answer) == index:
        print ("\n" + question + "\n")
        print ("\n >>> PASSED. \n")
        user_again = input("Do you want to try another difficulty? Write: y/n ").lower()
        if user_again == "y":
            return level_choice()
        elif user_again == "n":
            print("Don't forget to come back if you change your mind.")
        else:
            return "Well done anyways!"
    else:
        print("\n CORRECT. Running next:")
        return question

print (level_choice())
