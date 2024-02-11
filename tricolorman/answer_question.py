from enum import Enum, auto

class Color(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()

class Answer():
    def __init__(self, answer: str, color: Color):
        self.answer = answer
        self.color = color

class Question():
    def __init__(self, question: str, answers: list):
        self.question = question
        self.answers = answers
