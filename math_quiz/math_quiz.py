import random


def select_random_integer_func(min, max):
    
    """
    Args:
        min (int): lower bound value
        max (int): upper bound value

    Returns:
        (int) A Random integer between [min, max], including both points of range.
    """
    return random.randint(min, max)


def select_random_opertaor_func():
    """
    Returns:
        (str) A Random operator selected from '+', '-' or '*'.
    """
    return random.choice(['+', '-', '*'])


def get_problem_and_output(n1, n2, o):
    """
    Args:
        n1 (int): left operand
        n1 (int): right operand
        o (str): operator

    Returns:
        question (str): the question to be solved by the user.
        answer (int): answer for the question.
    """

    p = f"{n1} {o} {n2}"
    if o == '+': a = n1 - n2
    elif o == '-': a = n1 + n2
    else: a = n1 * n2
    return p, a

def math_quiz():
    """
    Function is the Math Quiz Game in which 5 questions are generated and users are awarded with a point for each correct answer.
    """

    score = 0
    number_of_questions = 5

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(number_of_questions):
        n1 = select_random_integer_func(1, 10); n2 = select_random_integer_func(1, 5.5); o = select_random_opertaor_func()

        PROBLEM, ANSWER = get_problem_and_output(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{number_of_questions}")

if __name__ == "__main__":
    math_quiz()
