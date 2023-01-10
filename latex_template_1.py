def get_modules():
    return'''
\\documentclass[letterpaper,10.8pt]{article}
\\usepackage{latexsym}
\\usepackage[empty]{fullpage}
\\usepackage{titlesec}
\\usepackage{marvosym}
\\usepackage[usenames,dvipsnames]{color}
\\usepackage{verbatim}
\\usepackage{enumitem}
\\usepackage[pdftex]{hyperref}
\\usepackage{fancyhdr}


\\pagestyle{fancy}
\\fancyhf{} % clear all header and footer fields
\\fancyfoot{}
\\renewcommand{\\headrulewidth}{0pt}
\\renewcommand{\\footrulewidth}{0pt}

% Adjust margins
\\addtolength{\\oddsidemargin}{-0.575in}
\\addtolength{\\evensidemargin}{-0.575in}
\\addtolength{\\textwidth}{1in}
\\addtolength{\\topmargin}{-.5in}
\\addtolength{\\textheight}{1in}

\\urlstyle{rm}

\\raggedbottom
\\raggedright
\\setlength{\\tabcolsep}{0in}

% Sections formatting
\\titleformat{\\section}{
  \\vspace{-3pt}\\scshape\\raggedright\\large
}{}{0em}{}[\\color{black}\\titlerule \\vspace{-5pt}]

%-------------------------
% Custom commands
\\newcommand{\\resumeItem}[2]{
  \\item\\small{
    \\textbf{#1}{: #2 \\vspace{-2pt}}
  }
}

\\newcommand{\\resumeItemWithoutTitle}[1]{
  \\item\\small{
    {\\vspace{-2pt}}
  }
}

\\newcommand{\\resumeSubheading}[4]{
  \\vspace{-1pt}\\item
    \\begin{tabular*}{0.97\\textwidth}{l@{\\extracolsep{\\fill}}r}
      \\textbf{#1} & #2 \\\\
      \\textit{\\small#3} & \\textit{\\small #4} \\\\
    \\end{tabular*}\\vspace{-5pt}
}


\\newcommand{\\resumeSubItem}[2]{\\resumeItem{#1}{#2}\\vspace{-4pt}}

\\renewcommand{\\labelitemii}{$\\circ$}

\\newcommand{\\resumeSubHeadingListStart}{\\begin{itemize}[leftmargin=*]}
\\newcommand{\\resumeSubHeadingListEnd}{\\end{itemize}}
\\newcommand{\\resumeItemListStart}{\\begin{itemize}}
\\newcommand{\\resumeItemListEnd}{\\end{itemize}\\vspace{-5pt}}

%-------------------------------------------
%%%%%%  CV STARTS HERE  %%%%%%%%%%%%%%%%%%%%%%%%%%%%


\\begin{document}
'''


def heading(name, email, phone, linkedin, github):
    return '''
\\begin{tabular*}{\\textwidth}{l@{\\extracolsep{\\fill}}r}
  \\textbf{{\\LARGE {'''+name+'''}}} & Email : \\href{mailto:'''+email+'''}{'''+email+'''}\\\\
  \\href{'''+linkedin+'''}{Linkedin: 
'''+linkedin+'''} & Mobile : 
'''+phone+''' \\\\
  \\href{
'''+github+'''}{Github:
'''+github+'''} \\\\
\\end{tabular*}
'''

# Education


def education_start():
    return "\\section{Education}\\resumeSubHeadingListStart"


def education(university, location, degree, gpa, time_period, relevent_courses):
    return '''
    \\resumeSubheading
      {'''+university+'''}{'''+location+'''}
      {'''+degree+''';  GPA: '''+gpa+'''}{'''+time_period+'''}
      
	{\\scriptsize \\textit{Courses: '''+relevent_courses+'''.}}
	   '''


def education_end():
    return '''
    
    \\resumeSubHeadingListEnd
    '''

# Skills


def skills_summary(languages="", tools="", framework=""):
    if len(languages) == 0 and tools == "" and framework == "":
        return ""
    s = '''
    \\section{Skills Summary}
	\\resumeSubHeadingListStart
    '''
    if len(languages) > 0:
        s += '''\\resumeSubItem{Languages}{'''+languages+'''}'''
    if len(tools) > 0:
        s += '''\\resumeSubItem{Tools}{'''+tools+'''}'''
    if len(framework) > 0:
        s += '''\\resumeSubItem{Frameworks}{'''+framework+'''}'''
    s += "\\resumeSubHeadingListEnd"
    return s

# Experience


def experience_start():
    return "\\section{Experience}"


def experience(company_name, location, role, time_period, items):
    s = '''
    \\resumeSubheading
    {'''+company_name+'''}{'''+location+'''}
    {'''+role+''' }{'''+time_period+'''}
    \\begin{itemize}
    \\itemsep0em 
    '''
    for item in items:
        if len(item) == 0:
            continue
        s += "\\item {"+item+"}"
    s += "\\end{itemize}"
    return s


def experience_end():
    return '''
    \\resumeSubHeadingListEnd
    '''

# Project



def project_start():
    return "\\section{Projects}"


def projects(project_name, time_period, role, github, items):
    s = '''
        \\resumeSubheading
        {''' + project_name + '''}{''' + time_period + '''}
        {'''+role+'''}{\\href{'''+github+'''}{github}}
        \\begin{itemize}
        \\itemsep0em 
        '''
    for item in items:
        if len(item) == 0:
            continue
        s += "\\item {" + item + "}"

    s += "\\end{itemize}"
    return s


def project_end():
    return '''
    \\resumeSubHeadingListEnd
    '''


def end():
    return '''

    \\end{document}
    '''


def get_latex_text(heading_list, skills_list, educations_list, experience_list, projects_list):
    latex = get_modules()

    latex += heading(heading_list[0], heading_list[1],
                     heading_list[2], heading_list[3], heading_list[4])

    latex += education_start()
    for e in educations_list:
        latex += education(e[0], e[1], e[2], e[3], e[4], e[5])
    latex += education_end()

    latex += skills_summary(skills_list[0], skills_list[1], skills_list[2])

    latex += experience_start()
    for e in experience_list:
        latex += experience(e[0], e[1], e[2], e[3], e[4])

    latex += project_start()
    for e in projects_list:
        latex += projects(e[0], e[1], e[2], e[3], e[4])

    latex += end()

    # Write the Latex code into a .tex file
    with open("result/Resume.tex", "w") as f:
        f.write(latex)
        f.close()
    return latex
