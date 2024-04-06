import tkinter as tk
from tkinter import messagebox

class GPACalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("GPA Calculator")

        # Dictionary to store grade points for each grade
        self.grade_points = {'A+': 4.3, 'A': 4.0, 'A-': 3.7,
                             'B+': 3.3, 'B': 3.0, 'B-': 2.7,
                             'C+': 2.3, 'C': 2.0, 'C-': 1.7,
                             'D+': 1.3, 'D': 1.0, 'F': 0.0}

        # Variables to store user input
        self.course_name_var = tk.StringVar()
        self.grade_var = tk.StringVar()
        self.credits_var = tk.DoubleVar()

        # List to store entered courses
        self.courses_list = []

        # GUI setup
        self.setup_gui()

    def calculate_gpa(self):
        total_credits = 0
        total_weighted_points = 0

        for course in self.courses_list:
            grade_points = self.grade_points.get(course['grade'], 0)
            total_weighted_points += grade_points * course['credits']
            total_credits += course['credits']

        if total_credits == 0:
            return 0.0

        gpa = total_weighted_points / total_credits
        return round(gpa, 2)

    def add_course(self):
        course_name = self.course_name_var.get()
        grade = self.grade_var.get()
        credits = self.credits_var.get()

        if not course_name or not grade or credits <= 0:
            messagebox.showerror("Error", "Please enter valid values for all fields.")
            return

        course = {'name': course_name, 'grade': grade, 'credits': credits}
        self.courses_list.append(course)

        self.update_course_listbox()
        self.clear_entry_fields()

    def remove_course(self):
        selected_index = self.courses_listbox.curselection()

        if not selected_index:
            messagebox.showerror("Error", "Please select a course to remove.")
            return

        index = int(selected_index[0])
        del self.courses_list[index]

        self.update_course_listbox()

    def update_course_listbox(self):
        self.courses_listbox.delete(0, tk.END)

        for course in self.courses_list:
            self.courses_listbox.insert(tk.END, f"{course['name']} - {course['grade']} ({course['credits']} credits)")

    def clear_entry_fields(self):
        self.course_name_var.set("")
        self.grade_var.set("")
        self.credits_var.set(0.0)

    def show_gpa(self):
        gpa = self.calculate_gpa()
        messagebox.showinfo("GPA Result", f"Your GPA is: {gpa}")

    def setup_gui(self):
        # Entry fields
        tk.Label(self.root, text="Course Name:").grid(row=0, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.course_name_var).grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Grade:").grid(row=1, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.grade_var).grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Credits:").grid(row=2, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.credits_var).grid(row=2, column=1, padx=10, pady=10)

        # Buttons
        tk.Button(self.root, text="Add Course", command=self.add_course).grid(row=3, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text="Remove Course", command=self.remove_course).grid(row=4, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text="Calculate GPA", command=self.show_gpa).grid(row=5, column=0, columnspan=2, pady=10)

        # Listbox to display entered courses
        self.courses_listbox = tk.Listbox(self.root, width=40, height=10)
        self.courses_listbox.grid(row=6, column=0, columnspan=2, pady=10)

# Create the main Tkinter window
root = tk.Tk()
gpa_calculator = GPACalculator(root)

# Run the Tkinter event loop
root.mainloop()
