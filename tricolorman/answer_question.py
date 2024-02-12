from enum import Enum, auto


class Color(Enum):
    """Enumeration of colors."""

    RED = auto()
    GREEN = auto()
    BLUE = auto()


class Answer:
    """
    This class contains the answer text and the corresponding color.

    :param text: The text of the question.
    :type text: str
    :param color: A color corresponding to the answer.
    :type answers: Color
    :return: A Answer object initialized with the provided text and color.
    :rtype: Answer

    """

    def __init__(self, text: str, color: Color) -> None:
        """Initialize the Answer object."""
        self.text = text
        self.color = color

    def __repr__(self) -> str:
        """Return a string representation of the Answer."""
        return f"A: text={self.text} | color={self.color}"


class Question:
    """This class contains the question text and the array of answers.

    :param text: The text of the question.
    :type text: str
    :param answers: A list of Answer objects representing possible answers to the question.
    :type answers: list[Answer]
    :return: A Question object initialized with the provided text and answers.
    :rtype: Question
    """

    def __init__(self, text: str, answers: list):
        """Initialize the Question object."""
        self.text = text
        self.answers = answers

    def __repr__(self) -> str:
        """Return a string representation of the Question."""
        return f"Q: {self.text} for {self.answers}"
