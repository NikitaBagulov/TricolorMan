from enum import Enum, auto

class Color(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()

class Answer():
    def __init__(self, text: str, color: Color):
        self.text = text
        self.color = color

    def __repr__(self) -> str:
        return f"A: {self.text} {self.color}"

class Question():
    def __init__(self, text: str, answers: list):
        self.text = text
        self.answers = answers

    def __repr__(self) -> str:
        return f"Q: {self.text} for {self.answers}"
