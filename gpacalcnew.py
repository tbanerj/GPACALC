import tkinter as tk
from tkinter import messagebox
import sqlite3

# Create SQLite database and table
conn = sqlite3.connect('gpa_data.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        gpa REAL NOT NULL
    )
''')
conn.commit()

class GPA_Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("GPA Calculator")

        # Create variables
        self.name_var = tk.StringVar()
        self.gpa_var = tk.DoubleVar()

        # Labels
        tk.Label(root, text="Student Name:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        tk.Label(root, text="GPA:").grid(row=1, column=0, padx=10, pady=10, sticky="e")

        # Entry widgets
        tk.Entry(root, textvariable=self.name_var).grid(row=0, column=1, padx=10, pady=10)
        tk.Entry(root, textvariable=self.gpa_var).grid(row=1, column=1, padx=10, pady=10)

        # Buttons
        tk.Button(root, text="Calculate GPA", command=self.calculate_gpa).grid(row=2, column=0, columnspan=2, pady=10)
        tk.Button(root, text="Save Data", command=self.save_data).grid(row=3, column=0, columnspan=2, pady=10)

    def calculate_gpa(self):
        # Add GPA calculation logic here
        messagebox.showinfo("GPA Calculation", "GPA calculation logic goes here.")

    def save_data(self):
        name = self.name_var.get()
        gpa = self.gpa_var.get()

        # Insert data into SQLite database
        cursor.execute("INSERT INTO students (name, gpa) VALUES (?, ?)", (name, gpa))
        conn.commit()
        messagebox.showinfo("Data Saved", "Student data saved successfully.")

if __name__ == "__main__":
    root = tk.Tk()
    app = GPA_Calculator(root)
    root.mainloop()
