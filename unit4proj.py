# Stephen Randall
# 9/29/17
# Folder: Unit4Project File: unit4proj.py
# This program is simply a quiz on aeronautical fun facts, contains three different formats of questions
# Multiple choice, true false, and numerical questions.

print("Welcome to this quiz!")
print("This quiz will be on the topic: Commercial Airlines/Commercial Airplanes")
print("Ready? Ok! Let's start with the first question.")


def question_one():
    """
    Function asks the user a question and gives the options available. Asks the user for their input, once they input
    their answer evaluates their answer with if and else statements. If correct prints out a congrats message and
    adds 1 point to player_score. If is incorrect, prints incorrect message return no points to player_score.
    !!!ALL OTHER FUNCTIONS FOLLOW SAME FORMAT!!! EXCLUDING "final_score"
    :return: Return the updated score to player_score in main function.
    """
    print("(1.) British Airlines is one of the most well known airliners to date. What is their hub city?")
    print("(a) London Gatwick LGW")
    print("(b) London Stansted Airport STN")
    print("(c) Heathrow Airport LHR")
    print("(d) Luton Airport LTN ")
    question_one_answer = input("Answer?")
    if question_one_answer in ["c", "C", "(c)"]:
        print("That's correct! Congratulations")
        return 1
    else:
        print("Sorry, that's incorrect")
        return 0


def question_two():
    print("(2.) The 787 is a part of the new up and coming modern fleet, but when was its first test flight?")
    print("(a) April 11, 2007")
    print("(b) May 7, 2012")
    print("(c) November 23, 2010")
    print("(d) December 15, 2009")
    question_two_answer = input("Answer?")
    if question_two_answer in ["d", "D", "(d)"]:
        print("Awesome! That one was a hard one, good work.")
        return 1
    else:
        print("Sorry that's wrong. Don't feel bad though, that was a hard one.")
        return 0


def question_three():
    print("(3.) What is the approximate max flight time for an A380 at maximum payload? ")
    print("Please enter your answer in the form of a decimal ex: 8.0 thus meaning 8 hours.")
    question_three_answer = float(input("Answer?"))
    if question_three_answer == 17.4:
        print("That's right! You must be really good at this, that one was hard!")
        return 1
    else:
        print("Sorry, that's incorrect.")
        return 0


def question_four():
    print("(4.) What is the max passenger capacity of a 737-900ER?")
    print("Please enter your answer as a whole number. Ex:45 meaning 45 passengers.")
    question_four_answer = int(input("Answer?"))
    if question_four_answer == 215:
        print("Correct! Nice!")
        return 1
    else:
        print("Sorry, that's incorrect.")
        return 0


def question_five():
    print("(5.)True or False, upon the release of the 787 the entire fleet was grounded for systematical issues?")
    print("Enter 1 for true or 0 for false")
    question_five_answer = int(input("Answer?"))
    question_five_answer = bool(question_five_answer)
    if question_five_answer:
        print("You're right!")
        return 1
    else:
        print("Sorry that's wrong. Better luck next time!")
        return 0


def question_six():
    print("(6.) True or False, Boeing is seriously considering stopping the production of their iconic 747 series?")
    print("Enter 1 for true or 0 for false")
    question_six_answer = int(input("Answer?"))
    question_six_answer = bool(question_six_answer)
    if question_six_answer:
        print("That's right! Boeing is seriously considering stopping development due to low interest.")
        return 1
    else:
        print("Incorrect, better luck next time.")
        return 0


def question_seven():
    print("(7.) True or False, Continental Airlines merged with United Airlines")
    print("Enter 1 for true or 0 for false")
    question_seven_answer = int(input("Answer?"))
    question_seven_answer = bool(question_seven_answer)
    if question_seven_answer:
        print("Good Job! That's correct, they merged in 2012")
        return 1
    else:
        print("Sorry, that's not correct. They merged back in 2012")
        return 0


def question_eight():
    print("(8.)When was the concorde's last flight?")
    print("(a) December 7, 1998")
    print("(b) October 24, 2003")
    print("(c) November 25, 2001")
    print("(d) January 3, 2002")
    question_eight_answer = input("Answer?")
    if question_eight_answer in ["b", "B", "(b)", "(B)"]:
        print("Correct!")
        return 1
    else:
        print("Sorry, that's wrong.")
        return 0


def question_nine():
    print("(9.) When was the tragic concorde plane crash?")
    print("(a) July 25, 2000")
    print("(b) November 3, 2001")
    print("(c) June 4, 2000")
    print("(d) May 15, 1999")
    question_nine_answer = input("Answer?")
    if question_nine_answer in ["a", "A", "(a)", "(A)"]:
        print("Correct!")
        return 1
    else:
        print("Incorrect")
        return 0


def question_ten():
    print("(10.) Last question, the A380 is a piece of mechanical beauty. What is the max fuel load?")
    print("Please input you answer as a number with no commas. ex: 100000")
    question_ten_answer = int(input("Answer?"))
    if question_ten_answer == 320000:
        print("Correct!")
        return 1
    else:
        print("Incorrect")
        return 0


def final_score(player_score):
    """
    This function sorts the player_score value into fun messages based on the users knowledge(score).
    :param player_score: Receives player_score value from main.
    :return: returns the correct statement to print out based on player's score.
    """
    if player_score == 10:
        print("Wow! You're really good! You got everything right!")
    elif 6 <= player_score <= 9:
        print("You did pretty well, keep studying those plane facts. Remember to Keep Calm and Fly On")
    else:
        print("You need to revise your basic plane facts, shaking my head.")


def main():
    player_score = 0
    player_score += question_one()
    player_score += question_two()
    player_score += question_three()
    player_score += question_four()
    player_score += question_five()
    player_score += question_six()
    player_score += question_seven()
    player_score += question_eight()
    player_score += question_nine()
    player_score += question_ten()
    final_score(player_score)

    print("Your final score was:", player_score)
main()
