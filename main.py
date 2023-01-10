from tkinter import *
from tkinter import ttk
from ui_handler import *
from latex_template_1 import get_latex_text
import os

root = Tk()
root.geometry("600x800")
root.title("Resume Builder")

# Header
heading_frame = Frame(root)

full_name_textbox = Text(heading_frame, height=1, width=50)
full_name_label = Label(heading_frame, text="Full Name:")
full_name_label.grid(row=1, column=1)
full_name_textbox.grid(row=1, column=2)

email = Text(heading_frame, height=1, width=50)
email_label = Label(heading_frame, text="Email:")
email_label.grid(row=2, column=1)
email.grid(row=2, column=2)

phone_number = Text(heading_frame, height=1, width=50)
phone_number_label = Label(heading_frame, text="Phone Number:")
phone_number_label.grid(row=3, column=1)
phone_number.grid(row=3, column=2)

linkedin_profile_url = Text(heading_frame, height=1, width=50)
linkedin_profile_url_label = Label(heading_frame, text="LinkedIn URL:")
linkedin_profile_url_label.grid(row=4, column=1)
linkedin_profile_url.grid(row=4, column=2)

github_profile_url = Text(heading_frame, height=1, width=50)
github_profile_url_label = Label(heading_frame, text="Github URL:")
github_profile_url_label.grid(row=5, column=1)
github_profile_url.grid(row=5, column=2)

# Skills
skills_frame = Frame(root)
languages = Text(skills_frame, height=1, width=50)
frameworks = Text(skills_frame, height=1, width=50)
tools = Text(skills_frame, height=1, width=50)

Label(skills_frame, text="Languages:").grid(row=1, column=1)
languages.grid(row=1, column=2)
Label(skills_frame, text="Frameworks:").grid(row=2, column=1)
frameworks.grid(row=2, column=2)
Label(skills_frame, text="Tools:").grid(row=3, column=1)
tools.grid(row=3, column=2)

# Education
education_frame = Frame(root)
education_button = Button(education_frame, text="Add Education",
                          command=lambda: education_top_level(education_frame))
education_button.pack()

# Experience
experience_frame = Frame(root)
experience_button = Button(experience_frame, text="Add Experience",
                           command=lambda: experience_top_level(experience_frame))
experience_button.pack()

# Projects
project_frame = Frame(root)
project_button = Button(project_frame, text="Add Project",
                        command=lambda: project_top_level(project_frame))
project_button.pack()

# Make the resume
def get_data():
    name = full_name_textbox.get("1.0", END).split("\n")[0]
    email_text = email.get("1.0", END).split("\n")[0]
    phone_number_text = phone_number.get("1.0", END).split("\n")[0]
    linkedin = linkedin_profile_url.get("1.0", END).split("\n")[0]
    github = github_profile_url.get("1.0", END).split("\n")[0]
    heading = [name, email_text, phone_number_text, linkedin, github]

    languages_text = languages.get("1.0", END).split("\n")[0]
    framework_text = frameworks.get("1.0", END).split("\n")[0]
    tools_text = tools.get("1.0", END).split("\n")[0]
    skills = [languages_text, framework_text, tools_text]

    get_latex_text(heading, skills, EDUCATIONS, EXPERIENCES, PROJECTS)
    os.system("cd result && pdflatex -interaction=nonstopmode Resume.tex")

# Pack Everything
Label(root, text="Personal Information", font=(
    "Arial", 20)).pack(anchor="w", pady=10)
heading_frame.pack(anchor="w")
Label(root, text="Skills", font=("Arial", 16)).pack(anchor="w", pady=5)
skills_frame.pack(anchor="w")
Label(root, text="Education", font=("Arial", 16)).pack(anchor="w", pady=5)
education_frame.pack()
Label(root, text="Experience", font=("Arial", 16)).pack(anchor="w", pady=15)
experience_frame.pack()
Label(root, text="Projects", font=("Arial", 16)).pack(anchor="w", pady=5)
project_frame.pack()
Button(root, text="Submit", command=get_data).pack()

root.mainloop()