from .answer_question import Color, Answer, Question
import os
import sys
import pkg_resources
from random import shuffle


class Tricolorman:
    """Class representing the Tricolorman test application."""

    def __init__(self):
        """Initializes the Tricolorman test application."""
        self.__questions = []
        self.__red_count = 0
        self.__green_count = 0
        self.__blue_count = 0
        try:
            self.__questions = self.__load_test()
        except FileNotFoundError as e:
            print(f"Error loading test questions: {e}")

    def __load_test(self) -> list:
        """Loads questions from a file and creates Question instances."""
        questions = []
        try:
            color_sets = [
                [Color.GREEN, Color.BLUE, Color.RED],
                [Color.BLUE, Color.RED, Color.GREEN],
                [Color.RED, Color.GREEN, Color.BLUE],
            ]

            questions_path = self.search_file(sys.prefix, "questions.txt")

            with open(questions_path, "r", encoding="utf-8") as file:
                lines = file.readlines()
                num_questions = len(lines) // 4
                for i in range(0, num_questions * 4, 4):
                    question_text = lines[i].strip()
                    answer_texts = [
                        line.strip() for line in lines[i + 1 : i + 4]
                    ]
                    color_set = color_sets[
                        i // (len(lines) // len(color_sets))
                    ]
                    answers = [
                        Answer(answer_text[:-1], color)
                        for answer_text, color in zip(answer_texts, color_set)
                    ]
                    question = Question(question_text, answers)
                    questions.append(question)
        except Exception as e:
            print(f"Error loading test questions: {e}")
        return questions

    @staticmethod
    def search_file(directory, filename):
        """Search for a file in the given directory and its subdirectories."""
        for root, dirs, files in os.walk(directory):
            if filename in files:
                return os.path.join(root, filename)
        return None

    def get_result_images(self):
        """Retrieves images based on the test results."""
        try:
            result = self.get_results()
            max_percent = max(result.values())
            dominant_colors = [
                color
                for color, percent in result.items()
                if percent == max_percent
            ]

            image_sequence = []
            for dominant_color in dominant_colors:
                if dominant_color == "Красный":
                    name = "red"
                elif dominant_color == "Зеленый":
                    name = "green"
                elif dominant_color == "Синий":
                    name = "blue"
                else:
                    continue
                for i in range(1, 5):
                    image_sequence.append(
                        self.search_file(sys.prefix,
                            f"{name}{i}.png",
                        )
                    )
            image_sequence.append(
                self.search_file(sys.prefix,
                    "general.png"
                )
            )
            return image_sequence
        except Exception as e:
            print(f"Ошибка при получении изображений результата: {e}")
            return []




    def __shuffle_question_and_answers(self):
        """Shuffles the order of questions and answers."""
        shuffle(self.__questions)
        for question in self.__questions:
            shuffle(question.answers)

    def get_questions(self) -> list:
        """
        Retrieves shuffled questions for the test.

        :return: A list of Question instances.
        :rtype: list
        """
        try:
            self.__shuffle_question_and_answers()
            return self.__questions
        except Exception as e:
            print(f"Error getting questions: {e}")
            return []

    def set_color(self, color: str):
        """
        Updates the color count based on the selected answer.

        :param color: The color selected as the answer.
        :type color: str
        """
        try:
            match getattr(Color, color[6:]):
                case Color.RED:
                    self.__red_count+=1
                case Color.GREEN:
                    self.__green_count+=1
                case Color.BLUE:
                    self.__blue_count+=1
        except AttributeError as e:
            print(f"Error setting color: {e}")

    def get_results(self):
        """
        Calculates the percentage of each color in the test results.

        :return: A dictionary containing color percentages.
        :rtype: dict
        """
        try:
            red_percent = round(self.__red_count / len(self.__questions) * 100, 2)
            green_percent = round(self.__green_count / len(self.__questions) * 100, 2)
            blue_percent = round(self.__blue_count / len(self.__questions) * 100, 2)
            return {
                "Красный": red_percent,
                "Зеленый": green_percent,
                "Синий": blue_percent,
            }
        except ZeroDivisionError as e:
            print(f"Error calculating results: {e}")
            return {}
