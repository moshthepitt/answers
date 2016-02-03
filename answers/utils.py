from decimal import Decimal
from .models import Answer
from questions.models import MultipleChoiceQuestion


def calculate_multichoice_score(review):
    """
    This functions calculates the score of a Quiz
    by comparing the answer to the question's expected
    correct answer
    returns a Dict that looks like so:
    {
        correct: 6,
        question_count: 10,
        score: 0.6
    }
    """
    answers = Answer.objects.filter(review=review)
    correct = 0
    for answer in answers:
        if isinstance(answer.question, MultipleChoiceQuestion):
            correct_answers = answer.question.multiplechoiceoption_set.filter(correct_answer=True)
            if answer.answer in correct_answers:
                # this is correct
                correct += 1
            else:
                # this is wrong
                pass
    result = {
        'correct': correct,
        'question_count': answers.count(),
        'score': Decimal(correct) / Decimal(answers.count())
    }
    return result
