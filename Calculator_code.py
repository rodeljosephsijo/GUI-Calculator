import tkinter as tk

LIGHT_GREY="#F5F5F5"
class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0, 0)
        self.window.title("Project_1 Calculator")

        self.display_frame = self.create_display_frame()
        self.buttons_frame = self.create_buttons_frame()

    def create_display_frame(self):
        frame=tk.Frame(self.window, height=221, bg=LIGHT_GREY)
        frame.pack(expand=True, fill="both")
        return frame
    
    def create_buttons_frame(self):
        frame=tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()  # Instantiate class
    calc.run()           # Call the run method