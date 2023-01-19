from tkinter import *
from gpt_summary import get_summary_for_resume,get_summary_for_projects
import datetime

EXPERIENCES = []
PROJECTS = []
EDUCATIONS = []
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]
years = [i for i in range(1950, 2100)]

def project_top_level(root):
    global PROJECTS
    top = Toplevel()
    top.title("Resume Builder-Projects")
    # Project Frame
    project_name = Text(top, height=1, width=40)
    project_name_label = Label(top, text="Project Title")
    project_name_label.grid(row=1, column=1)
    project_name.grid(row=1, column=2)

    git_hub_text = Text(top, height=1, width=40)
    git_hub_label = Label(top, text="Github Link")
    git_hub_label.grid(row=3, column=1)
    git_hub_text.grid(row=3, column=2)

    role = Text(top, height=1, width=40)
    role_label = Label(top, text="Role")
    role_label.grid(row=2, column=1)
    role.grid(row=2, column=2)

    year_variable = StringVar()
    year_variable.set(datetime.date.today().year)
    year1_variable = StringVar()
    year1_variable.set(datetime.date.today().year)

    variable = StringVar()
    variable.set("Jan")
    frame = Frame(top)
    start_date_dropdown = OptionMenu(frame, variable, *months)
    start_date_year = OptionMenu(frame,year_variable, *years)
    Label(frame, text="Start Date").grid(row=1, column=1)
    start_date_dropdown.grid(row=1, column=2)
    start_date_year.grid(row=1, column=3)

    variable1 = StringVar()
    variable1.set("Jan")
    end_date_dropdown = OptionMenu(frame, variable1, *months)
    end_date_year = OptionMenu(frame,year1_variable, *years)
    Label(frame, text="End Date").grid(row=2, column=1)
    end_date_dropdown.grid(row=2, column=2)
    end_date_year.grid(row=2, column=3)

    frame.grid(row=4, column=1)
    jd = Text(top, height=10, width=50)
    Label(top, text="Explain your work in your own words:").grid(row=5, column=1)
    jd.grid(row=5, column=2)

    # Callback to Submit Button
    def get_data():
        project_name_text = project_name.get("1.0", END).split("\n")[0]
        github_text = git_hub_text.get("1.0", END).split("\n")[0]
        role_text = role.get("1.0", END).split("\n")[0]
        jd_text = jd.get("1.0", END)
        jd_text = get_summary_for_projects(jd_text)
        start_year_text = year_variable.get()
        start_month_text = variable.get()
        end_month_text = variable1.get()
        end_year_text = year1_variable.get()
        time_period = start_month_text+" "+start_year_text + \
            " - "+end_month_text+" "+end_year_text
        PROJECTS.append([project_name_text, time_period,
                        role_text, github_text, jd_text.split("\n")])
        Label(root, text=project_name_text+"...").pack()
        top.destroy()
    submit = Button(top, text="submit", command=get_data)
    submit.grid(row=7, column=1)


def experience_top_level(root):
    global EXPERIENCES
    top = Toplevel()
    top.title("Resume Builder-Experience")
    company_name = Text(top, height=1, width=40)
    company_name_label = Label(top, text="Company Name")
    company_name_label.grid(row=1, column=1)
    company_name.grid(row=1, column=2)

    location = Text(top, height=1, width=40)
    location_label = Label(top, text="Location(State, Country)")
    location_label.grid(row=2, column=1)
    location.grid(row=2, column=2)

    role = Text(top, height=1, width=40)
    role_label = Label(top, text="Role")
    role_label.grid(row=3, column=1)
    role.grid(row=3, column=2)

    year_variable = StringVar()
    year_variable.set(datetime.date.today().year)
    year1_variable = StringVar()
    year1_variable.set(datetime.date.today().year)

    variable = StringVar()
    variable.set("Jan")
    frame = Frame(top)
    start_date_dropdown = OptionMenu(frame, variable, *months)
    start_date_year = OptionMenu(frame,year_variable, *years)
    Label(frame, text="Start Date").grid(row=1, column=1)
    start_date_dropdown.grid(row=1, column=2)
    start_date_year.grid(row=1, column=3)

    variable1 = StringVar()
    variable1.set("Jan")
    end_date_dropdown = OptionMenu(frame, variable1, *months)
    end_date_year = OptionMenu(frame,year1_variable, *years)
    Label(frame, text="End Date").grid(row=2, column=1)
    end_date_dropdown.grid(row=2, column=2)
    end_date_year.grid(row=2, column=3)

    frame.grid(row=4, column=1)
    jd = Text(top, height=10, width=50)
    Label(top, text="Explain your work in your own words:").grid(row=5, column=1)
    jd.grid(row=5, column=2)

    # Callback to Submit Button
    def get_data():
        company_name_text = company_name.get("1.0", END).split("\n")[0]
        location_text = location.get("1.0", END).split("\n")[0]
        role_text = role.get("1.0", END).split("\n")[0]
        jd_text = jd.get("1.0", END)
        jd_text = get_summary_for_resume(jd_text).replace("%", "\\%")
        start_year_text = year_variable.get()
        start_month_text = variable.get()
        end_month_text = variable1.get()
        end_year_text = year1_variable.get()
        time_period = start_month_text+" "+start_year_text + \
            " - "+end_month_text+" "+end_year_text
        EXPERIENCES.append([company_name_text, location_text,
                           role_text, time_period, jd_text.split("\n")])
        Label(root, text=company_name_text).pack()
        top.destroy()
    submit = Button(top, text="submit", command=get_data)
    submit.grid(row=7, column=1)


def education_top_level(root):
    top = Toplevel()
    top.title("Resume Builder-Education")
    university_name = Text(top, height=1, width=40)
    location_name = Text(top, height=1, width=40)
    degree_name = Text(top, height=1, width=40)
    gpa = Text(top, height=1, width=4)

    year_variable = StringVar()
    year_variable.set(datetime.date.today().year)
    year1_variable = StringVar()
    year1_variable.set(datetime.date.today().year)
    variable = StringVar()
    variable.set("Jan")

    frame = Frame(top)
    start_date_dropdown = OptionMenu(frame, variable, *months)
    start_date_year = OptionMenu(frame,year_variable, *years)
    Label(frame, text="Start Date").grid(row=1, column=1)
    start_date_dropdown.grid(row=1, column=2)
    start_date_year.grid(row=1, column=3)

    variable1 = StringVar()
    variable1.set("Jan")

    end_date_dropdown = OptionMenu(frame, variable1, *months)
    end_date_year = OptionMenu(frame,year1_variable, *years)
    Label(frame, text="End Date").grid(row=2, column=1)
    end_date_dropdown.grid(row=2, column=2)
    end_date_year.grid(row=2, column=3)

    relevent_courses = Text(top, height=2, width=40)

    Label(top, text="University Name:").grid(row=1, column=1)
    university_name.grid(row=1, column=2)

    Label(top, text="Location(State, Country):").grid(row=2, column=1)
    location_name.grid(row=2, column=2)

    Label(top, text="Degree:").grid(row=3, column=1)
    degree_name.grid(row=3, column=2)

    Label(top, text="GPA:").grid(row=4, column=1)
    gpa.grid(row=4, column=2)

    Label(top, text="Relevant Coursework(Seperate Courses with ',') :").grid(
        row=5, column=1)
    relevent_courses.grid(row=5, column=2)
    frame.grid(row=6, column=1)
    
    # Callback to Submit Button
    def get_data():
        university_name_text = university_name.get("1.0", END).split("\n")[0]
        location_name_text = location_name.get("1.0", END).split("\n")[0]
        degree_name_text = degree_name.get("1.0", END).split("\n")[0]
        gpa_text = gpa.get("1.0", END).split("\n")[0]
        relevent_courses_text = relevent_courses.get("1.0", END).split("\n")[0]
        start_year_text = year_variable.get()
        start_month_text = variable.get()
        end_month_text = variable1.get()
        end_year_text = year1_variable.get()
        time_period = start_month_text + " " + start_year_text + \
            " - " + end_month_text + " " + end_year_text
        EDUCATIONS.append([university_name_text, location_name_text,
                          degree_name_text, gpa_text, time_period, relevent_courses_text])
        Label(root, text=university_name_text).pack()
        top.destroy()

    Button(top, text="Submit", command=get_data).grid(row=7, column=1)
