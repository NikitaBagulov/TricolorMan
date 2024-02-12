from tricolorman import Tricolorman
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk


class TricolormanGUI:
    """TricolormanGUI class represents the graphical user interface for the Tricolorman test application."""

    def __init__(self, master):
        """Initialize TricolormanGUI instance."""
        self.master = master
        self.__questions = []
        self.__test = None
        self.__current_question_index = 0
        self.__selected_answer = tk.StringVar()
        master.title("Tricolorman test")

        self.center_frame = tk.Frame(master)
        self.center_frame.pack(expand=True, fill="x")

        self.label = tk.Label(
            self.center_frame,
            text="Нажмите кнопку для начала теста",
            font=("Arial", 12),
        )
        self.label.pack(anchor="n")

        self.start_button = tk.Button(
            self.center_frame,
            text="Начать тест",
            command=self.__start_test,
            font=("Arial", 12),
            bg="blue",
            fg="white",
            width=20,
            height=2,
        )
        self.start_button.pack(anchor="n")

        exit_button = tk.Button(
            self.center_frame,
            text="Выйти из приложения",
            command=self.master.destroy,
            bg="red",
            fg="white",
        )
        exit_button.pack(anchor="n")

    def __start_test(self):
        """Start the Tricolorman test."""
        try:
            self.__test = Tricolorman()
            self.__questions = self.__test.get_questions()
            self.__show_question()
        except Exception as e:
            print(f"Error starting the test: {e}")

    def __show_question(self):
        """Display the current question."""
        self.__selected_answer.set(None)

        for widget in self.center_frame.winfo_children():
            widget.destroy()
        exit_button = tk.Button(
            self.master,
            text="Выйти из приложения",
            command=self.master.destroy,
            bg="red",
            fg="white",
            width=25,
            height=1,
        )
        exit_button.place(relx=0.05, rely=0.05, anchor="nw")
        exit_button.lift()

        try:
            current_question = self.__questions[self.__current_question_index]
            self.question_label = tk.Label(
                self.center_frame,
                text=current_question.text,
                font=("Arial", 14, "bold"),
                wraplength=630,
            )
            self.question_label.pack(anchor="n")

            self.answer_radio_buttons = []
            self.radio_buttons_frame = tk.Frame(self.center_frame)
            self.radio_buttons_frame.pack(expand=True, anchor="n")
            for answer_index, answer in enumerate(current_question.answers):
                answer_radio_button = tk.Radiobutton(
                    self.radio_buttons_frame,
                    text=f"{answer_index+1}. {answer.text}",
                    variable=self.__selected_answer,
                    value=answer.color,
                    font=("Arial", 12),
                    anchor="w",
                )
                answer_radio_button.pack(anchor="nw")
                self.answer_radio_buttons.append(answer_radio_button)
            self.next_button = tk.Button(
                self.center_frame,
                text="Следующий вопрос",
                command=self.__next_question,
                font=("Arial", 12),
                bg="green",
                fg="white",
                width=20,
                height=2,
                state="disabled",
            )
            self.next_button.pack(anchor="n")
            self.__selected_answer.trace_add(
                "write", self.__selected_answer_changed
            )
        except Exception as e:
            print(f"Error showing the question: {e}")

    def __selected_answer_changed(self, *args):
        """Handle the change in selected answer."""
        if self.__selected_answer.get():
            self.next_button.config(state="normal")
        else:
            self.next_button.config(state="disabled")

    def __next_question(self):
        """Move to the next question."""
        try:
            self.__test.set_color(self.__selected_answer.get())

            self.__current_question_index += 1

            if self.__current_question_index < len(self.__questions):
                self.__show_question()
            else:
                self.__show_results()
        except Exception as e:
            print(f"Error moving to the next question: {e}")

    def __show_results(self):
        """Display the test results."""
        try:
            for widget in self.center_frame.winfo_children():
                widget.destroy()
            graph_frame = tk.Frame(self.center_frame, width=1020)
            graph_frame.pack(expand=True, fill="x", side="top", anchor="n")

            button_frame = tk.Frame(self.center_frame)
            button_frame.pack(expand=True, side="bottom", anchor="s")

            result_labels = []
            result_values = []
            colors = ["red", "green", "blue"]
            for color, percent in self.__test.get_results().items():
                result_labels.append(color)
                result_values.append(percent)
            fig = Figure(figsize=(6, 6), facecolor="#F0F0F0", edgecolor="gray")
            ax = fig.add_subplot(111)
            ax.pie(
                result_values,
                labels=result_labels,
                autopct="%1.1f%%",
                startangle=140,
                colors=colors,
            )
            ax.axis("equal")

            canvas = FigureCanvasTkAgg(fig, master=graph_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(expand=True)

            show_image_button = tk.Button(
                button_frame,
                text="Узнать результат",
                command=self.__show_result_image,
                font=("Arial", 12),
                bg="blue",
                fg="white",
                width=20,
                height=2,
            )
            show_image_button.pack(pady=10)
        except Exception as e:
            print(f"Error showing the results: {e}")

    def __show_result_image(self):
        """Display the result image."""
        try:
            for widget in self.center_frame.winfo_children():
                widget.destroy()
            self.radio_buttons_frame.destroy()
            result_images = self.__test.get_result_images()

            window_width = self.master.winfo_width()
            window_height = self.master.winfo_height()

            self.image_frames = []
            for image_path in result_images:
                image_frame = tk.Frame(self.center_frame, bg="white")
                image_frame.pack(expand=True, fill="both")
                image_frame.configure(bg="white")

                image = Image.open(image_path)

                resized_image = image.resize((window_width, window_height))

                tk_image = ImageTk.PhotoImage(resized_image)

                image_label = tk.Label(image_frame, image=tk_image)
                image_label.image = tk_image
                image_label.pack(expand=True, fill="both")

                self.image_frames.append(image_frame)
            self.current_image_index = 0
            self.image_frames[self.current_image_index].tkraise()

            next_button = tk.Button(
                self.center_frame,
                text="Далее",
                command=self.__show_next_image,
                bg="green",
                fg="white",
                width=25,
                height=3,
            )
            next_button.place(relx=0.95, rely=0.05, anchor="ne")
            next_button.lift()

            exit_button = tk.Button(
                self.center_frame,
                text="Выйти из приложения",
                command=self.master.destroy,
                bg="red",
                fg="white",
                width=25,
                height=1,
            )
            exit_button.place(relx=0.05, rely=0.05, anchor="nw")
            exit_button.lift()
        except Exception as e:
            print(f"Error showing the result image: {e}")

    def __show_next_image(self):
        """Display the next image."""
        try:
            self.image_frames[self.current_image_index].pack_forget()
            self.current_image_index += 1
            if self.current_image_index >= len(self.image_frames) - 1:
                for widget in self.center_frame.winfo_children():
                    if (
                        isinstance(widget, tk.Button)
                        and widget["text"] == "Далее"
                    ):
                        widget.destroy()
                return
            self.image_frames[self.current_image_index].pack(
                expand=True, fill="both"
            )
        except Exception as e:
            print(f"Error showing the next image: {e}")
