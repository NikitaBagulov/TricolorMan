import os
import pytest
import tkinter as tk
from tricolorman import Tricolorman
from tricolorman import TricolormanGUI


class TestTricolorman:
    @pytest.fixture
    def tricolorman_instance(self):
        return Tricolorman()

    def test_load_questions(self, tricolorman_instance):
        questions = tricolorman_instance.get_questions()
        assert questions, "Questions list should not be empty"
        for question in questions:
            assert len(question.answers) == 3, "Each question should have 3 answers"

    def test_results_calculation(self, tricolorman_instance):
        for _ in range(0, 10):
            tricolorman_instance.set_color("Color.RED")
        for _ in range(0, 5):
            tricolorman_instance.set_color("Color.GREEN")
        results = tricolorman_instance.get_results()
        assert (
            results["Красный"] == 66.67
        ), "Red percentage should be approximately 66.67%"

    def test_color_setting(self, tricolorman_instance):
        tricolorman_instance.set_color("Color.RED")
        assert (
            tricolorman_instance._Tricolorman__red_count == 1
        ), "Red count should be incremented"
        tricolorman_instance.set_color("InvalidColor")
        assert (
            tricolorman_instance._Tricolorman__red_count == 1
        ), "Red count should not change for invalid color"

    def test_get_result_images(self, tricolorman_instance):
        images = tricolorman_instance.get_result_images()
        assert images, "Image list should not be empty"
        for image in images:
            assert os.path.exists(image), f"Image file '{image}' should exist"


@pytest.fixture
def root():
    root = tk.Tk()
    yield root
    root.destroy()


class TestTricolormanGUI:
    @pytest.fixture
    def tricolorman_gui(self, root):
        return TricolormanGUI(root)

    def test_initialization(self, tricolorman_gui):
        assert tricolorman_gui.master.title() == "Tricolorman test"
        assert tricolorman_gui._TricolormanGUI__questions == []
        assert tricolorman_gui._TricolormanGUI__test == None
        assert tricolorman_gui._TricolormanGUI__current_question_index == 0
        assert tricolorman_gui._TricolormanGUI__selected_answer.get() == ""

    def test_start_test(self, tricolorman_gui):
        tricolorman_gui._TricolormanGUI__start_test()
        assert tricolorman_gui._TricolormanGUI__test is not None

    def test_show_question(self, tricolorman_gui):
        tricolorman_gui._TricolormanGUI__start_test()
        tricolorman_gui._TricolormanGUI__show_question()
        assert tricolorman_gui.question_label.cget("text") != ""
        assert len(tricolorman_gui.answer_radio_buttons) > 0
        assert tricolorman_gui.next_button["state"] == "disabled"

    def test_selected_answer_changed(self, tricolorman_gui):
        tricolorman_gui._TricolormanGUI__start_test()
        tricolorman_gui._TricolormanGUI__show_question()
        tricolorman_gui._TricolormanGUI__selected_answer.set("Color.RED")
        assert tricolorman_gui._TricolormanGUI__selected_answer.get() == "Color.RED"

    def test_next_question(self, tricolorman_gui):
        tricolorman_gui._TricolormanGUI__start_test()
        tricolorman_gui._TricolormanGUI__show_question()
        tricolorman_gui._TricolormanGUI__selected_answer.set("Color.RED")
        tricolorman_gui._TricolormanGUI__next_question()
        assert tricolorman_gui._TricolormanGUI__current_question_index == 1

    def test_show_results(self, tricolorman_gui):
        tricolorman_gui._TricolormanGUI__start_test()
        tricolorman_gui._TricolormanGUI__show_question()
        for _ in range(len(tricolorman_gui._TricolormanGUI__questions)):
            tricolorman_gui._TricolormanGUI__next_question()
        tricolorman_gui._TricolormanGUI__show_results()
        assert len(tricolorman_gui.center_frame.winfo_children()) == 2

    def test_show_result_image(self, tricolorman_gui):
        tricolorman_gui._TricolormanGUI__start_test()
        tricolorman_gui._TricolormanGUI__show_question()
        for _ in range(len(tricolorman_gui._TricolormanGUI__questions)):
            tricolorman_gui._TricolormanGUI__next_question()
        tricolorman_gui._TricolormanGUI__show_results()
        tricolorman_gui._TricolormanGUI__show_result_image()
        assert len(tricolorman_gui.center_frame.winfo_children()) == 15
