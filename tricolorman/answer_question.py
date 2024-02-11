from enum import Enum, auto

class Color(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()

class Answer():
    def __init__(self, answer: str, color: Color):
        self.answer = answer
        self.color = color

    def __str__(self) -> str:
        return f"A: {self.answer} {self.color}"

class Question():
    def __init__(self, question: str, answers: list):
        self.question = question
        self.answers = answers

    def __str__(self) -> str:
        return f"Q: {self.question} for {self.answers}"
