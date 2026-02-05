import tkinter as tk
from tkinter import filedialog

class CodeEditor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Flash Code Editor")
        self.geometry("1200x900")

        self.filename = None

        self.line_numbers = tk.Text(
            self, width=4, padx=4, takefocus=0,
            border=0, background="#f0f0f0"
        )
        self.text = tk.Text(
            self, undo=True, font=("Consolas", 11)
        )

        self.line_numbers.pack(side=tk.LEFT, fill=tk.Y)
        self.text.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.text.bind("<KeyRelease>", self.update_line_numbers)

        self.create_menu()
        self.update_line_numbers()

    def create_menu(self):
        menu = tk.Menu(self)
        file_menu = tk.Menu(menu, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_as)
        menu.add_cascade(label="File", menu=file_menu)
        self.config(menu=menu)

    def update_line_numbers(self, event=None):
        self.line_numbers.config(state="normal")
        self.line_numbers.delete("1.0", tk.END)

        line_count = self.text.index("end").split(".")[0]
        for i in range(1, int(line_count)):
            self.line_numbers.insert(tk.END, f"{i}\n")

        self.line_numbers.config(state="disabled")

    def open_file(self):
        path = filedialog.askopenfilename()
        if not path:
            return
        self.filename = path
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            self.text.delete("1.0", tk.END)
            self.text.insert(tk.END, f.read())
        self.update_line_numbers()

    def save_file(self):
        if not self.filename:
            self.save_as()
            return
        with open(self.filename, "w", encoding="utf-8") as f:
            f.write(self.text.get("1.0", tk.END))

    def save_as(self):
        path = filedialog.asksaveasfilename()
        if path:
            self.filename = path
            self.save_file()

if __name__ == "__main__":
    CodeEditor().mainloop()
