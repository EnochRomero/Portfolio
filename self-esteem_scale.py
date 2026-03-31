


def main():

    self_esteem_score = 0

    print("This program is an implementation of the Rosenberg Self-Esteem Scale. This program will show you ten statements that you could possibly apply to yourself. Please rate how much you agree with each of the statements by responding with one of these four letters:")

    print("A means you strongly agree")
    print("a means you agree")
    print("d means you disagree")
    print("D means you strongly disagree")

    input()

    answer = input("I feel that I am a person of worth, at least on an equal plane with others.")
    modifer = add_to_score(answer)
    self_esteem_score +=  modifer

    answer = input("I feel that I have a number of good qualities.")
    modifer = add_to_score(answer)
    self_esteem_score +=  modifer

    answer = input("All in all, I am inclined to feel that I am a failure.")
    modifer = subtract_from_score(answer)
    self_esteem_score +=  modifer

    answer = input("I am able to do things as well as most other people.")
    modifer = add_to_score(answer)
    self_esteem_score +=  modifer

    answer = input("I feel I do not have much to be proud of.")
    modifer = subtract_from_score(answer)
    self_esteem_score +=  modifer

    answer = input("I take a positive attitude toward myself.")
    modifer = add_to_score(answer)
    self_esteem_score +=  modifer

    answer = input("On the whole, I am satisfied with myself.")
    modifer = add_to_score(answer)
    self_esteem_score +=  modifer

    answer = input("I wish I could have more respect for myself.")
    modifer = subtract_from_score(answer)
    self_esteem_score +=  modifer

    answer = input("I certainly feel useless at times.")
    modifer = subtract_from_score(answer)
    self_esteem_score +=  modifer

    answer = input("At times I think I am no good at all.")
    modifer = subtract_from_score(answer)
    self_esteem_score +=  modifer

    if self_esteem_score < 15:
        print(f"Your final score if {self_esteem_score}. This score indicates you may have low self-esteem.")

    else:
        print(f"Your final score is {self_esteem_score}.")


def add_to_score(answer):
    
    if answer == "A":
        self_modifer = 3

    elif answer == "a":
        self_modifer = 2

    elif answer == "d":
        self_modifer = 1

    elif answer == "D":
        self_modifer =  0

    return self_modifer


def subtract_from_score(answer):

    if answer == "A":
        self_modifer = 0

    elif answer == "a":
        self_modifer = 1

    elif answer == "d":
        self_modifer = 2

    elif answer == "D":
        self_modifer =  3

    return self_modifer
    

main()