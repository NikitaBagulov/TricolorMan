from tricolorman import TricolormanGUI
import tkinter as tk

def main():
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    gui = TricolormanGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
